# -*- coding: utf-8 -*-
import functools
from typing import Callable, Dict, Optional, Tuple, Union

import e3nn_jax as e3j
from flax import linen
import flax.linen.dtypes
import flax.typing
import jax
import jax.numpy as jnp
from tensorial import gcnn, nn_utils

# Default activations used by gate
DEFAULT_ACTIVATIONS = linen.FrozenDict({'e': 'silu', 'o': 'tanh'})


class FourierKANLayer(linen.Module):
    features: int
    grid_size: int
    kernel_init: flax.typing.Initializer = flax.linen.initializers.lecun_normal
    bias_init: flax.typing.Initializer = flax.linen.initializers.zeros_init()
    with_bias: bool = False
    dtype: Optional[flax.typing.Dtype] = None
    param_dtype: flax.typing.Dtype = jnp.float32

    @linen.compact
    def __call__(self, inputs: Union[jnp.ndarray, e3j.IrrepsArray]):
        kernel = self.param(
            'kernel',
            self.kernel_init,
            (2, self.features, jnp.shape(inputs)[-1], self.grid_size),
            self.param_dtype,
        )
        if self.with_bias:
            bias = self.param('bias', self.bias_init, (
                1,
                self.features,
            ), self.param_dtype)
        else:
            bias = None
        inputs, kernel, bias = linen.dtypes.promote_dtype(inputs, kernel, bias, dtype=self.dtype)

        xshp = inputs.shape
        outshape = xshp[0:-1] + (self.features,)
        # inputs = jnp.reshape(inputs, (-1, self.inputdim))
        # Starting at 1 because constant terms are in the bias
        k = jnp.reshape(jnp.arange(1, self.grid_size + 1), (1, 1, 1, self.grid_size))
        xrshp = jnp.reshape(inputs, (inputs.shape[0], 1, inputs.shape[1], 1))
        # This should be fused to avoid materializing memory
        c = jnp.cos(k * xrshp)
        s = jnp.sin(k * xrshp)
        # We compute the interpolation of the various functions defined by their fourier coefficient for each input coordinates and we sum them
        y = jnp.sum(c * kernel[0], (-2, -1))
        y = y + jnp.sum(s * kernel[1], (-2, -1))
        if self.with_bias:
            y = y + bias

        y = jnp.reshape(y, outshape)
        return y


class MultiLayerKan(flax.linen.Module):

    list_neurons: Tuple[int, ...]
    gradient_normalization: Union[str, float] = None
    with_bias: bool = False

    @flax.linen.compact
    def __call__(
        self, inputs: Union[jnp.ndarray, e3j.IrrepsArray]
    ) -> Union[jnp.ndarray, e3j.IrrepsArray]:
        """Evaluate the MLP

        Input and output are either `jax.numpy.ndarray` or `IrrepsArray`.
        If the input is a `IrrepsArray`, it must contain only scalars.

        Args:
            inputs (IrrepsArray): input of shape ``[..., input_size]``

        Returns:
            IrrepsArray: output of shape ``[..., list_neurons[-1]]``
        """
        gradient_normalization = self.gradient_normalization
        if gradient_normalization is None:
            gradient_normalization = e3j.config('gradient_normalization')
        if isinstance(gradient_normalization, str):
            gradient_normalization = {'element': 0.0, 'path': 1.0}[gradient_normalization]

        if isinstance(inputs, e3j.IrrepsArray):
            if not inputs.irreps.is_scalar():
                raise ValueError('MLP only works on scalar (0e) input.')
            inputs = inputs.array
            output_irrepsarray = True
        else:
            output_irrepsarray = False

        for i, h in enumerate(self.list_neurons):
            alpha = 1 / inputs.shape[-1]
            d = FourierKANLayer(
                features=h,
                grid_size=5,
                with_bias=self.with_bias,
                kernel_init=flax.linen.initializers.normal(
                    stddev=jnp.sqrt(alpha)**(1.0 - gradient_normalization)
                ),
                bias_init=flax.linen.initializers.zeros,
                param_dtype=inputs.dtype,
            )
            inputs = jnp.sqrt(alpha)**gradient_normalization * d(inputs)

        if output_irrepsarray:
            inputs = e3j.IrrepsArray(e3j.Irreps(f'{inputs.shape[-1]}x0e'), inputs)
        return inputs


# -*- coding: utf-8 -*-


class InteractionBlock(linen.Module):
    """NequIP style interaction block.

    Implementation based on
        https://github.com/mir-group/nequip/blob/main/nequip/nn/_interaction_block.py
    and
        https://github.com/mariogeiger/nequip-jax/blob/main/nequip_jax/nequip.py

    :param irreps_out: the irreps of the output node features
    :param radial_num_layers: the number of layers in the radial MLP
    :param radial_num_neurons: the number of neurons per layer in the radial MLP
    :param avg_num_neighbours: average number of neighbours of each node, used for normalisation
    :param self_connection: If True, self connection will be applied at end of interaction
    """

    irreps_out: e3j.Irreps = 4 * e3j.Irreps('0e + 1o + 2e')
    # Radial
    radial_num_layers: int = 1
    radial_num_neurons: int = 8

    avg_num_neighbours: float = 1.0
    self_connection: bool = True
    activations: Union[str, Dict[str, str]] = DEFAULT_ACTIVATIONS

    num_species: int = 1

    def setup(self):
        self._gate = functools.partial(  # pylint: disable=attribute-defined-outside-init
            e3j.gate,
            even_act=nn_utils.get_jaxnn_activation(self.activations['e']),
            odd_act=nn_utils.get_jaxnn_activation(self.activations['o']),
            even_gate_act=nn_utils.get_jaxnn_activation(self.activations['e']),
            odd_gate_act=nn_utils.get_jaxnn_activation(self.activations['o']),
        )

    @linen.compact
    def __call__(
        self,
        node_features: e3j.IrrepsArray,
        edge_features: e3j.IrrepsArray,
        edge_length_embeddings: e3j.IrrepsArray,
        senders,
        receivers,
        node_species: Optional[jax.Array] = None,
        edge_mask: Optional[jax.Array] = None,
    ) -> e3j.IrrepsArray:
        """
        # A NequIP interaction made up of the following steps

        # - Linear on nodes
        # - tensor product + aggregate
        # - divide by sqrt(average number of neighbors)
        # - concatenate
        # - Linear on nodes
        # - Gate non-linearity
        """
        num_nodes = node_features.shape[0]

        output_irreps = e3j.Irreps(self.irreps_out
                                   ).regroup()  # The irreps to use for the output node features

        # First linear, stays in current irreps space
        messages = e3j.flax.Linear(node_features.irreps, name='linear_up')(node_features)[senders]

        # Interaction between nodes and edges
        edge_features = e3j.tensor_product(
            messages, edge_features, filter_ir_out=output_irreps + '0e'
        )

        # Make a compound message
        messages = e3j.concatenate([messages.filter(output_irreps + '0e'), edge_features]).regroup()

        # Now, based on the messages irreps, create the radial MLP that maps from inter-atomic
        # distances to tensor product weights
        mlp = MultiLayerKan(
            (self.radial_num_neurons,) * self.radial_num_layers + (messages.irreps.num_irreps,),
            with_bias=False,  # do not use bias so that R(0) = 0
        )

        # Get weights for the tensor product from our full-connected MLP
        if edge_mask is not None:
            edge_length_embeddings = jnp.where(
                nn_utils.prepare_mask(edge_mask, edge_length_embeddings),
                edge_length_embeddings,
                0.0,
            )
        weights = mlp(edge_length_embeddings)
        if edge_mask is not None:
            weights = jnp.where(
                nn_utils.prepare_mask(edge_mask, edge_length_embeddings), weights, 0.0
            )
        messages = messages * weights

        # Pass the messages, summing those from edges onto nodes
        node_features = e3j.scatter_sum(messages, dst=receivers, output_size=num_nodes)

        # Normalisation
        node_features = node_features / jnp.sqrt(self.avg_num_neighbours)

        gate_irreps = output_irreps.filter(keep=messages.irreps)
        num_non_scalar = gate_irreps.filter(drop='0e + 0o').num_irreps
        gate_irreps = gate_irreps + (num_non_scalar * e3j.Irrep('0e'))

        # Second linear, now we create any extra gate scalars
        node_features = e3j.flax.Linear(gate_irreps, name='linear_down')(node_features)

        # self-connection: species weighted tensor product that maps to current irreps space
        if self.self_connection:
            self_connection = e3j.flax.Linear(
                gate_irreps,
                num_indexed_weights=self.num_species,
                name='self_connection',
                force_irreps_out=True,
            )(node_species, node_features)

            node_features = node_features + self_connection

        # Apply non-linearity
        node_features = self._gate(node_features)
        return node_features
