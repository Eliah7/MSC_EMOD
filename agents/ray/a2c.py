from ray.rllib.algorithms.a3c import A3CConfig
from ray import tune, air
import ray
import json
from env.environment import MalariaEnvironment
from ray.tune.logger import pretty_print
ray.init(ignore_reinit_error=True, num_cpus=1, local_mode=True)

# Parallel environments
from ray.tune.registry import register_env

def env_creator(env_config):
    return MalariaEnvironment()  # return an env instance

register_env("MalariaEnvironment", env_creator)
env = MalariaEnvironment()

config = A3CConfig()
# Print out some default values.
# print(config.sample_async)  
# Update the config object.
config = config.training(lr=0.01)
# config = config.rollouts(num_rollout_workers=1)
config = config.framework()

# Set the config object's env.
config = config.environment(env="MalariaEnvironment") 
# Use to_dict() to get the old-style python config dict
# when running with tune.

pretty_print(config.to_dict())


algo = config.build()  
for i in range(10):
    # print(f"Iteration Count: {i}")
    training_results = algo.train()

print(pretty_print(training_results))

# algo.train() 
# evaluation_duration
# metrics_episode_collection_timeout_s
# tune.Tuner(  
#     "A3C",
#     param_space=config.to_dict(),
#      run_config=air.RunConfig(local_dir="./agents/ray/results", name="test_experimen2t")
# ).fit()
