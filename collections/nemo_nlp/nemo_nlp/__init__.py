# Copyright 2019 AI Applications Design Team at NVIDIA. All Rights Reserved.
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
# ==============================================================================

from .data import *
from .transformer_nm import TransformerEncoderNM, TransformerDecoderNM, \
    TransformerLogSoftmaxNM, PaddedSmoothedCrossEntropyLossNM, \
    BeamSearchTranslatorNM, GreedyLanguageGeneratorNM
from .bert import MaskedLanguageModelingLossNM, \
    SentenceClassificationLogSoftmaxNM, NextSentencePredictionLossNM, \
    LossAggregatorNM, TokenClassificationLoss, SequenceClassifier, \
    JointIntentSlotLoss, ZerosLikeNM, \
    JointIntentSlotClassifier
from .nlp_utils import read_intent_slot_outputs
from . import transformer, huggingface

from .callbacks import *

from nemo.core import Backend


name = "nemo_nlp"
backend = Backend.PyTorch
__version__ = "0.8"
