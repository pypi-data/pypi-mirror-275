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


import math
from typing import TypeVar

import torch as th
from torch import distributions as pyd
from torch.nn import functional as F

from rllte.common.prototype import BaseDistribution

SelfSquashedNormal = TypeVar("SelfSquashedNormal", bound="SquashedNormal")


class TanhTransform(pyd.transforms.Transform):
    # Borrowed from https://github.com/denisyarats/pytorch_sac/blob/master/agent/actor.py.
    """Tanh transformation."""

    domain = pyd.constraints.real
    codomain = pyd.constraints.interval(-1.0, 1.0)
    bijective = True
    sign = +1

    def __init__(self, cache_size=1):
        super().__init__(cache_size=cache_size)

    @staticmethod
    def atanh(x):
        return 0.5 * (x.log1p() - (-x).log1p())

    def __eq__(self, other):
        return isinstance(other, TanhTransform)

    def _call(self, x):
        return x.tanh()

    def _inverse(self, y):
        return self.atanh(y)

    def log_abs_det_jacobian(self, x, y):
        return 2.0 * (math.log(2.0) - x - F.softplus(-2.0 * x))


class SquashedNormal(BaseDistribution):
    """Squashed normal distribution for `Box` tasks."""

    def __init__(self) -> None:
        super().__init__()

    def __call__(self: SelfSquashedNormal, mu: th.Tensor, sigma: th.Tensor) -> SelfSquashedNormal:
        """Create the distribution.

        Args:
            mu (th.Tensor): The mean of the distribution.
            sigma (th.Tensor): The standard deviation of the distribution.

        Returns:
            Squashed normal distribution instance.
        """
        self.mu = mu
        self.sigma = sigma
        self.dist = pyd.TransformedDistribution(
            base_distribution=pyd.Normal(loc=mu, scale=sigma),
            transforms=[TanhTransform()],
        )
        return self

    def sample(self, sample_shape: th.Size = th.Size()) -> th.Tensor:  # B008
        """Generates a sample_shape shaped sample or sample_shape shaped
            batch of samples if the distribution parameters are batched.

        Args:
            sample_shape (th.Size): The size of the sample to be drawn.

        Returns:
            A sample_shape shaped sample.
        """
        return self.dist.sample(sample_shape)

    def rsample(self, sample_shape: th.Size = th.Size()) -> th.Tensor:  # B008
        """Generates a sample_shape shaped reparameterized sample or sample_shape shaped
            batch of reparameterized samples if the distribution parameters are batched.

        Args:
            sample_shape (th.Size): The size of the sample to be drawn.

        Returns:
            A sample_shape shaped sample.
        """
        return self.dist.rsample(sample_shape)

    @property
    def mean(self) -> th.Tensor:
        """Return the transformed mean."""
        loc = self.mu
        for tr in self.dist.transforms:
            loc = tr(loc)
        return loc

    @property
    def mode(self) -> th.Tensor:
        """Returns the mode of the distribution."""
        return self.mean

    def log_prob(self, actions: th.Tensor) -> th.Tensor:
        """Scores the sample by inverting the transform(s) and computing the score using
            the score of the base distribution and the log abs det jacobian.
        Args:
            actions (th.Tensor): The actions to be evaluated.

        Returns:
            The log_prob value.
        """
        return self.dist.log_prob(actions)
