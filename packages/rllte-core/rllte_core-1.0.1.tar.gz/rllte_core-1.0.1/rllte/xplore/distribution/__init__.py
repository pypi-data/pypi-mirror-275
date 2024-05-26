# =============================================================================
# MIT License

# Copyright (c) 2023 Reinforcement Learning Evolution Foundation

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# =============================================================================

# sampling distribution
from .bernoulli import Bernoulli as Bernoulli
from .categorical import Categorical as Categorical
from .diagonal_gaussian import DiagonalGaussian as DiagonalGaussian

# kl divergence
from .kl import kl_bernoulli_bernoulli as kl_bernoulli_bernoulli
from .kl import kl_categorical_categorical as kl_categorical_categorical
from .kl import kl_diagonal_gaussian_diagonal_gaussian as kl_diagonal_gaussian_diagonal_gaussian
from .multi_categorical import MultiCategorical as MultiCategorical

# action noise
from .normal_noise import NormalNoise as NormalNoise
from .ornstein_uhlenbeck_noise import OrnsteinUhlenbeckNoise as OrnsteinUhlenbeckNoise
from .squashed_normal import SquashedNormal as SquashedNormal
from .truncated_normal_noise import TruncatedNormalNoise as TruncatedNormalNoise
