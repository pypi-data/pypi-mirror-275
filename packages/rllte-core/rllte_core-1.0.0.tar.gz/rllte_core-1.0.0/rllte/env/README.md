Integrating RL environments in RLLTE is incredibly easy and efficient!

## Menu
1. [Installation](#installation)
2. [Usage](#usage)

## Installation

Assuming you are running inside a conda environment.

### Atari
```
pip install ale-py==0.8.1
```

### Craftax

You will need a Jax GPU-enabled conda environment:

```
conda create -n craftax jaxlib=*=*cuda* jax python=3.11 -c conda-forge
pip install craftax
pip install brax
pip install -e .[envs]
pip install -U "jax[cuda12_pip]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html 
```

### DMC
```
pip install dm-control
```

### SuperMarioBros
```
pip install gym-super-mario-bros==7.4.0
```

### Minigrid
```
pip install minigrid
```

### Miniworld
```
pip install miniworld
```

### Procgen
```
pip install procgen
```

### Envpool
```
pip install envpool
```

## Usage

Each environment has a `make_env()` function in `rllte/env/<your_RL_env>/__init__.py` and its necessary wrappers in `rllte/env/<your_RL_env>/wrappers.py`. To add your custom environments, simply follow the same logic as the currently available environments, and the RL training will work flawlessly!

## Example training

```
from rllte.agent import PPO
from rllte.env import (
    make_mario_env,
    make_envpool_vizdoom_env,
    make_envpool_procgen_env,
    make_minigrid_env,
    make_envpool_atari_env,
    make_craftax_env
)

# define params
device = "cuda"

# define environment
env = make_craftax_env(
        num_envs=32,
        device=device,
    )

# define agent
agent = PPO(
    env=env,
    device=device
)
        
# start training
agent.train(
    num_train_steps=10_000_000,
)
```
