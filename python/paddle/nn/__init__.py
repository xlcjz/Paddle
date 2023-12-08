#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from . import functional, initializer, quant, utils  # noqa: F401
from .clip import ClipGradByGlobalNorm, ClipGradByNorm, ClipGradByValue
from .decode import BeamSearchDecoder, dynamic_decode

# TODO: remove loss, keep it for too many used in unittests
from .layer import loss  # noqa: F401
from .layer.activation import (
    CELU,
    ELU,
    GELU,
    GLU,
    SELU,
    Hardshrink,
    Hardsigmoid,
    Hardswish,
    Hardtanh,
    LeakyReLU,
    LogSigmoid,
    LogSoftmax,
    Maxout,
    Mish,
    PReLU,
    ReLU,
    ReLU6,
    RReLU,
    Sigmoid,
    Silu,
    Softmax,
    Softmax2D,
    Softplus,
    Softshrink,
    Softsign,
    Swish,
    Tanh,
    Tanhshrink,
    ThresholdedReLU,
)
from .layer.common import (
    AlphaDropout,
    Bilinear,
    CosineSimilarity,
    Dropout,
    Dropout2D,
    Dropout3D,
    Embedding,
    EmbeddingBag,
    Flatten,
    Fold,
    Identity,
    Linear,
    Pad1D,
    Pad2D,
    Pad3D,
    Unflatten,
    Unfold,
    Upsample,
    UpsamplingBilinear2D,
    UpsamplingNearest2D,
    ZeroPad2D,
)

# TODO: import all neural network related api under this directory,
# including layers, linear, conv, rnn etc.
from .layer.container import LayerDict, LayerList, ParameterList, Sequential
from .layer.conv import (
    Conv1D,
    Conv1DTranspose,
    Conv2D,
    Conv2DTranspose,
    Conv3D,
    Conv3DTranspose,
)
from .layer.distance import PairwiseDistance
from .layer.layers import Layer
from .layer.loss import (
    BCELoss,
    BCEWithLogitsLoss,
    CosineEmbeddingLoss,
    CrossEntropyLoss,
    CTCLoss,
    GaussianNLLLoss,
    HingeEmbeddingLoss,
    HSigmoidLoss,
    KLDivLoss,
    L1Loss,
    MarginRankingLoss,
    MSELoss,
    MultiLabelSoftMarginLoss,
    MultiMarginLoss,
    NLLLoss,
    PoissonNLLLoss,
    RNNTLoss,
    SmoothL1Loss,
    SoftMarginLoss,
    TripletMarginLoss,
    TripletMarginWithDistanceLoss,
)
from .layer.norm import (
    BatchNorm,
    BatchNorm1D,
    BatchNorm2D,
    BatchNorm3D,
    GroupNorm,
    InstanceNorm1D,
    InstanceNorm2D,
    InstanceNorm3D,
    LayerNorm,
    LocalResponseNorm,
    SpectralNorm,
    SyncBatchNorm,
)
from .layer.pooling import (
    AdaptiveAvgPool1D,
    AdaptiveAvgPool2D,
    AdaptiveAvgPool3D,
    AdaptiveMaxPool1D,
    AdaptiveMaxPool2D,
    AdaptiveMaxPool3D,
    AvgPool1D,
    AvgPool2D,
    AvgPool3D,
    MaxPool1D,
    MaxPool2D,
    MaxPool3D,
    MaxUnPool1D,
    MaxUnPool2D,
    MaxUnPool3D,
)
from .layer.rnn import (
    GRU,
    LSTM,
    RNN,
    BiRNN,
    GRUCell,
    LSTMCell,
    RNNCellBase,
    SimpleRNN,
    SimpleRNNCell,
)
from .layer.transformer import (
    MultiHeadAttention,
    Transformer,
    TransformerDecoder,
    TransformerDecoderLayer,
    TransformerEncoder,
    TransformerEncoderLayer,
)
from .layer.vision import ChannelShuffle, PixelShuffle, PixelUnshuffle
from .utils.spectral_norm_hook import spectral_norm  # noqa: F401

__all__ = [
    'BatchNorm',
    'CELU',
    'GroupNorm',
    'LayerNorm',
    'SpectralNorm',
    'BatchNorm1D',
    'BatchNorm2D',
    'BatchNorm3D',
    'InstanceNorm1D',
    'InstanceNorm2D',
    'InstanceNorm3D',
    'SyncBatchNorm',
    'LocalResponseNorm',
    'Embedding',
    'EmbeddingBag',
    'Linear',
    'Upsample',
    'UpsamplingNearest2D',
    'UpsamplingBilinear2D',
    'Pad1D',
    'Pad2D',
    'Pad3D',
    'CosineSimilarity',
    'Dropout',
    'Dropout2D',
    'Dropout3D',
    'Bilinear',
    'AlphaDropout',
    'Unfold',
    'Fold',
    'RNNCellBase',
    'SimpleRNNCell',
    'LSTMCell',
    'GRUCell',
    'RNN',
    'BiRNN',
    'SimpleRNN',
    'LSTM',
    'GRU',
    'dynamic_decode',
    'MultiHeadAttention',
    'Maxout',
    'Softsign',
    'Transformer',
    'MSELoss',
    'LogSigmoid',
    'BeamSearchDecoder',
    'ClipGradByNorm',
    'ReLU',
    'PairwiseDistance',
    'BCEWithLogitsLoss',
    'SmoothL1Loss',
    'MaxPool3D',
    'AdaptiveMaxPool2D',
    'Hardshrink',
    'Softplus',
    'KLDivLoss',
    'AvgPool2D',
    'L1Loss',
    'LeakyReLU',
    'AvgPool1D',
    'AdaptiveAvgPool3D',
    'AdaptiveMaxPool3D',
    'NLLLoss',
    'PoissonNLLLoss',
    'Conv1D',
    'Sequential',
    'Hardswish',
    'Conv1DTranspose',
    'AdaptiveMaxPool1D',
    'TransformerEncoder',
    'Softmax',
    'Softmax2D',
    'ParameterList',
    'Conv2D',
    'Softshrink',
    'Hardtanh',
    'TransformerDecoderLayer',
    'CrossEntropyLoss',
    'GELU',
    'GLU',
    'SELU',
    'Silu',
    'Conv2DTranspose',
    'CTCLoss',
    'RNNTLoss',
    'ThresholdedReLU',
    'AdaptiveAvgPool2D',
    'MaxPool1D',
    'Layer',
    'TransformerDecoder',
    'Conv3D',
    'Tanh',
    'Conv3DTranspose',
    'Flatten',
    'AdaptiveAvgPool1D',
    'Tanhshrink',
    'HSigmoidLoss',
    'PReLU',
    'TransformerEncoderLayer',
    'AvgPool3D',
    'MaxPool2D',
    'MarginRankingLoss',
    'LayerList',
    'ClipGradByValue',
    'BCELoss',
    'Hardsigmoid',
    'ClipGradByGlobalNorm',
    'LogSoftmax',
    'Sigmoid',
    'Swish',
    'Mish',
    'PixelShuffle',
    'PixelUnshuffle',
    'ChannelShuffle',
    'ELU',
    'ReLU6',
    'LayerDict',
    'ZeroPad2D',
    'MaxUnPool1D',
    'MaxUnPool2D',
    'MaxUnPool3D',
    'MultiLabelSoftMarginLoss',
    'HingeEmbeddingLoss',
    'Identity',
    'CosineEmbeddingLoss',
    'RReLU',
    'MultiMarginLoss',
    'TripletMarginWithDistanceLoss',
    'TripletMarginLoss',
    'SoftMarginLoss',
    'GaussianNLLLoss',
    'Unflatten',
]
