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


from typing import Optional

import gymnasium as gym
import torch as th
from torch.nn import functional as F

from rllte.agent import utils
from rllte.common.prototype import OffPolicyAgent
from rllte.common.type_alias import VecEnv
from rllte.xploit.encoder import IdentityEncoder, TassaCnnEncoder
from rllte.xploit.policy import OffPolicyDetActorDoubleCritic
from rllte.xploit.storage import NStepReplayStorage
from rllte.xplore.augmentation import RandomShift
from rllte.xplore.distribution import TruncatedNormalNoise


class DrQv2(OffPolicyAgent):
    """Data Regularized Q-v2 (DrQv2) agent.
        Based on: https://github.com/facebookresearch/drqv2

    Args:
        env (VecEnv): Vectorized environments for training.
        eval_env (VecEnv): Vectorized environments for evaluation.
        tag (str): An experiment tag.
        seed (int): Random seed for reproduction.
        device (str): Device (cpu, cuda, ...) on which the code should be run.
        pretraining (bool): Turn on the pre-training mode.

        num_init_steps (int): Number of initial exploration steps.
        storage_size (int): The capacity of the storage.
        feature_dim (int): Number of features extracted by the encoder.
        batch_size (int): Number of samples per batch to load.
        lr (float): The learning rate.
        eps (float): Term added to the denominator to improve numerical stability.
        hidden_dim (int): The size of the hidden layers.
        critic_target_tau: The critic Q-function soft-update rate.
        update_every_steps (int): The agent update frequency.
        stddev_clip (float): The exploration std clip range.
        init_fn (str): Parameters initialization method.

    Returns:
        DrQv2 agent instance.
    """

    def __init__(
        self,
        env: VecEnv,
        eval_env: Optional[VecEnv] = None,
        tag: str = "default",
        seed: int = 1,
        device: str = "cpu",
        pretraining: bool = False,
        num_init_steps: int = 2000,
        storage_size: int = 1000000,
        feature_dim: int = 50,
        batch_size: int = 256,
        lr: float = 1e-4,
        eps: float = 1e-8,
        hidden_dim: int = 1024,
        critic_target_tau: float = 0.01,
        update_every_steps: int = 2,
        stddev_clip: float = 0.3,
        init_fn: str = "orthogonal",
    ) -> None:
        super().__init__(
            env=env,
            eval_env=eval_env,
            tag=tag,
            seed=seed,
            device=device,
            pretraining=pretraining,
            num_init_steps=num_init_steps,
        )

        # hyper parameters
        self.lr = lr
        self.eps = eps
        self.critic_target_tau = critic_target_tau
        self.update_every_steps = update_every_steps
        self.stddev_clip = stddev_clip

        # default encoder
        if len(self.obs_shape) == 3:
            encoder = TassaCnnEncoder(observation_space=env.observation_space, feature_dim=feature_dim)
        elif len(self.obs_shape) == 1:
            feature_dim = self.obs_shape[0]  # type: ignore
            encoder = IdentityEncoder(
                observation_space=env.observation_space, feature_dim=feature_dim  # type: ignore[assignment]
            )

        # default distribution
        self.action_space: gym.spaces.Box
        dist = TruncatedNormalNoise()

        # create policy
        policy = OffPolicyDetActorDoubleCritic(
            observation_space=env.observation_space,
            action_space=env.action_space,
            feature_dim=feature_dim,
            hidden_dim=hidden_dim,
            opt_class=th.optim.Adam,
            opt_kwargs=dict(lr=lr, eps=eps),
            init_fn=init_fn,
        )

        # default storage
        storage = NStepReplayStorage(
            observation_space=env.observation_space,
            action_space=env.action_space,
            storage_size=storage_size,
            device=device,
            batch_size=batch_size,
            num_envs=self.num_envs,
        )

        # default augmentation
        aug = RandomShift(pad=4).to(self.device)

        # set all the modules [essential operation!!!]
        self.set(encoder=encoder, policy=policy, storage=storage, distribution=dist, augmentation=aug)

    def update(self) -> None:
        """Update the agent and return training metrics such as actor loss, critic_loss, etc."""
        if self.global_step % self.update_every_steps != 0:
            return None

        # sample a batch
        batch = self.storage.sample()

        # obs augmentation
        if self.aug is not None:
            obs = self.aug(batch.observations)
            next_obs = self.aug(batch.next_observations)
        else:
            obs = batch.observations
            next_obs = batch.next_observations

        # encode
        encoded_obs = self.policy.encoder(obs)
        with th.no_grad():
            encoded_next_obs = self.policy.encoder(next_obs)

        # update criitc
        self.update_critic(encoded_obs, batch.actions, batch.rewards, batch.discounts, encoded_next_obs)

        # update actor (do not udpate encoder)
        self.update_actor(encoded_obs.detach())

        # udpate critic target
        utils.soft_update_params(self.policy.critic, self.policy.critic_target, self.critic_target_tau)

    def update_critic(
        self,
        obs: th.Tensor,
        actions: th.Tensor,
        rewards: th.Tensor,
        discount: th.Tensor,
        next_obs: th.Tensor,
    ) -> None:
        """Update the critic network.

        Args:
            obs (th.Tensor): Observations.
            actions (th.Tensor): Actions.
            rewards (th.Tensor): Rewards.
            discounts (th.Tensor): discounts.
            next_obs (th.Tensor): Next observations.

        Returns:
            None.
        """

        with th.no_grad():
            # sample actions
            dist = self.policy.get_dist(next_obs)
            next_actions = dist.sample(clip=self.stddev_clip)
            next_obs_actions = th.concat([next_obs, next_actions], dim=-1)
            target_Q1, target_Q2 = self.policy.critic_target(next_obs_actions)
            target_V = th.min(target_Q1, target_Q2)
            target_Q = rewards + (discount * target_V)

        obs_actions = th.concat([obs, actions], dim=-1)
        Q1, Q2 = self.policy.critic(obs_actions)
        critic_loss = F.mse_loss(Q1, target_Q) + F.mse_loss(Q2, target_Q)

        # optimize encoder and critic
        self.policy.optimizers["encoder_opt"].zero_grad(set_to_none=True)
        self.policy.optimizers["critic_opt"].zero_grad(set_to_none=True)
        critic_loss.backward()
        self.policy.optimizers["critic_opt"].step()
        self.policy.optimizers["encoder_opt"].step()

        # record metrics
        self.logger.record("train/critic_loss", critic_loss.item())
        self.logger.record("train/critic_q1", Q1.mean().item())
        self.logger.record("train/critic_q2", Q2.mean().item())
        self.logger.record("train/critic_target_q", target_Q.mean().item())

    def update_actor(self, obs: th.Tensor) -> None:
        """Update the actor network.

        Args:
            obs (th.Tensor): Observations.

        Returns:
            None.
        """
        # sample actions
        dist = self.policy.get_dist(obs)
        actions = dist.sample(clip=self.stddev_clip)
        obs_actions = th.concat([obs, actions], dim=-1)
        Q1, Q2 = self.policy.critic(obs_actions)
        Q = th.min(Q1, Q2)

        actor_loss = -Q.mean()

        # optimize actor
        self.policy.optimizers["actor_opt"].zero_grad(set_to_none=True)
        actor_loss.backward()
        self.policy.optimizers["actor_opt"].step()

        # record metrics
        self.logger.record("train/actor_loss", actor_loss.item())
