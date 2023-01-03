import gym
from env.environment import MalariaEnvironment

if __name__ == '__main__':
    env = MalariaEnvironment()

    for i_episode in range(20):
        observation = env.reset()
        for t in range(100):
            action = env.action_space.sample()
  
            observation, reward, done, info, _ = env.step(action)

            print("EPISODE: {} REWARD: {}".format(i_episode, reward))