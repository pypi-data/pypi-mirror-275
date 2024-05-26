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


import json
import os
import re
from typing import Dict, List, Tuple

import numpy as np
import torch as th
from torch import nn

class RewardForwardFilter:
    """Reward forward filter."""
    def __init__(self, gamma: float = 0.99) -> None:
        self.rewems = None
        self.gamma = gamma

    def update(self, rews: th.Tensor) -> th.Tensor:
        if self.rewems is None:
            self.rewems = rews
        else:
            self.rewems = self.rewems * self.gamma + rews
        return self.rewems

class TorchRunningMeanStd:
    """Running mean and std for torch tensor."""

    def __init__(self, epsilon=1e-4, shape=(), device=None) -> None:
        self.mean = th.zeros(shape, device=device)
        self.var = th.ones(shape, device=device)
        self.count = epsilon

    def update(self, x) -> None:
        """Update mean and std with batch data."""
        with th.no_grad():
            batch_mean = th.mean(x, dim=0)
            batch_var = th.var(x, dim=0)
            batch_count = x.shape[0]
            self.update_from_moments(batch_mean, batch_var, batch_count)

    def update_from_moments(self, batch_mean, batch_var, batch_count) -> None:
        """Update mean and std with batch moments."""
        self.mean, self.var, self.count = self.update_mean_var_count_from_moments(
            self.mean, self.var, self.count, batch_mean, batch_var, batch_count
        )

    @property
    def std(self) -> th.Tensor:
        return th.sqrt(self.var)

    def update_mean_var_count_from_moments(
        self, mean, var, count, batch_mean, batch_var, batch_count
    ) -> Tuple[th.Tensor, th.Tensor, th.Tensor]:
        delta = batch_mean - mean
        tot_count = count + batch_count

        new_mean = mean + delta * batch_count / tot_count
        m_a = var * count
        m_b = batch_var * batch_count
        M2 = m_a + m_b + th.pow(delta, 2) * count * batch_count / tot_count
        new_var = M2 / tot_count
        new_count = tot_count

        return new_mean, new_var, new_count


class ExportModel(nn.Module):
    """Module for model export.

    Args:
        encoder (nn.Module): Encoder network.
        actor (nn.Module): Actor network.

    Returns:
        Export model format.
    """

    def __init__(self, encoder: nn.Module, actor: nn.Module) -> None:
        super().__init__()

        self.encoder = encoder
        self.actor = actor

    def forward(self, obs: th.Tensor) -> th.Tensor:
        """Only for model inference.

        Args:
            obs (th.Tensor): Observations.

        Returns:
            Deterministic actions.
        """
        return self.actor(self.encoder(obs))


class eval_mode:
    """Set the evaluation mode.

    Args:
        models (nn.Module): Models.

    Returns:
        None.
    """

    def __init__(self, *models) -> None:
        self.models = models

    def __enter__(self):
        self.prev_states = []
        for model in self.models:
            self.prev_states.append(model.training)
            model.mode(False)

    def __exit__(self, *args):
        for model, state in zip(self.models, self.prev_states):
            model.mode(state)
        return False


def to_numpy(xs: Tuple[th.Tensor, ...]) -> Tuple[np.ndarray, ...]:
    """Converts torch tensors to numpy arrays.

    Args:
        xs (Tuple[th.Tensor, ...]): Torch tensors.

    Returns:
        Numpy arrays.
    """
    for x in xs:
        print(x.size())
    return tuple(x[0].cpu().numpy() for x in xs)


def pretty_json(hp: Dict) -> str:
    """Returns a pretty json string.

    Args:
        hp (Dict): Hyperparameters.

    Returns:
        Pretty json string.
    """
    json_hp = json.dumps(hp, indent=2)
    return "".join("\t" + line for line in json_hp.splitlines(True))


def get_episode_statistics(infos: Dict) -> Tuple[List, List]:
    """Get the episode statistics.

    Args:
        infos (Dict): Information.

    Returns:
        Episode rewards and lengths.
    """
    if "episode" in infos.keys():
        indices = np.nonzero(infos["episode"]["l"])
        return infos["episode"]["r"][indices].tolist(), infos["episode"]["l"][indices].tolist()
    elif "final_info" in infos.keys():
        r: List = []
        l: List = []
        # to handle with the Atari environments
        for info in infos['final_info']:
            if info is not None and "episode" in info.keys():
                r.extend(info["episode"]["r"].tolist())
                l.extend(info["episode"]["l"].tolist())
        return r, l
    else:
        return [], []


def get_npu_name() -> str:
    """Get NPU name."""
    str_command = "npu-smi info"
    out = os.popen(str_command)
    text_content = out.read()
    out.close()
    lines = text_content.split("\n")
    npu_name_line = lines[6]
    name_part = npu_name_line.split("|")[1]
    npu_name = name_part.split()[-1]

    return npu_name


def schedule(schdl: str, step: int) -> float:
    """Exploration noise schedule.

    Args:
        schdl (str): Schedule mode.
        step (int): global training step.

    Returns:
        Standard deviation.
    """
    try:
        return float(schdl)
    except ValueError:
        match = re.match(r"linear\((.+),(.+),(.+)\)", schdl)
        if match:
            init, final, duration = (float(g) for g in match.groups())
            mix = np.clip(step / duration, 0.0, 1.0)
            return (1.0 - mix) * init + mix * final
        match = re.match(r"step_linear\((.+),(.+),(.+),(.+),(.+)\)", schdl)
        if match:
            init, final1, duration1, final2, duration2 = (float(g) for g in match.groups())
            if step <= duration1:
                mix = np.clip(step / duration1, 0.0, 1.0)
                return (1.0 - mix) * init + mix * final1
            else:
                mix = np.clip((step - duration1) / duration2, 0.0, 1.0)
                return (1.0 - mix) * final1 + mix * final2
    raise NotImplementedError(schdl)


def linear_lr_scheduler(optimizer, steps, total_num_steps, initial_lr) -> None:
    """Decreases the learning rate linearly.

    Args:
        optimizer (Optimizer): Wrapped optimizer.
        steps (int): Current step.
        total_num_steps (int): Total number of steps.
        initial_lr (float): Initial learning rate.
    
    Returns:
        None.
    """
    lr = initial_lr - (initial_lr * (steps / float(total_num_steps)))
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr