import gym
from env.environment import MalariaEnvironment
from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import DummyVecEnv

# Parallel environments
env = MalariaEnvironment()

# env = DummyVecEnv([lambda: env])

model = A2C("MultiInputPolicy", env, verbose=1, tensorboard_log='./tensorboard/a2c_malaria_tensorboard/')
model.learn(total_timesteps=25000)
model.save("a2c_cartpole")

del model # remove to demonstrate saving and loading

model = A2C.load("a2c_cartpole")

obs = env.reset()

n_episodes = 10
i = 0
while i < n_episodes:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    i = i + 1
    # env.render()