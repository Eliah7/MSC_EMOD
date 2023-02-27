from ray.rllib.algorithms.a3c import A3CConfig
from ray import tune, air
import ray
from env.environment import MalariaEnvironment

ray.init(ignore_reinit_error=True, num_cpus=4)

# Parallel environments
from ray.tune.registry import register_env

def env_creator(env_config):
    return MalariaEnvironment()  # return an env instance

register_env("MalariaEnvironment", env_creator)
env = MalariaEnvironment()

config = A3CConfig()
# Print out some default values.
print(config.sample_async)  
# Update the config object.
# config = config.training( 
    # lr=tune.grid_search([0.001, 0.0001]), use_critic=False)

# Set the config object's env.
config = config.environment(env="MalariaEnvironment") 
# Use to_dict() to get the old-style python config dict
# when running with tune.
tune.Tuner(  
    "A3C",
   # stop={"episode_reward_mean": 200},
    param_space=config.to_dict(),
     run_config=air.RunConfig(local_dir="./agents/ray/results", name="test_experiment")
).fit()