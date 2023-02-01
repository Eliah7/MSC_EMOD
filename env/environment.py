import gym
from gym.spaces import Dict, Box
import numpy as np
from utils.config_map import Configurations
from utils.campaigns_map import CampaignsMap


class MalariaEnvironment(gym.Env):
    def __init__(self, render_mode=None, size=5):
        self.config_map = Configurations(self)
        self.campaign_map = CampaignsMap(self)
        # Observations are dictionaries with the simulation configurations
        
        self.observation_space = Dict({"Transmission_Rate": Box(low=0.0, high=1.0, shape=(1,), dtype=np.float32)})

        # We have 2 dimensions each bounded from (0,1] for itns and another irs
        self.action_space =  Dict(
            {
                "ITNS": Box(low=0.0, high=1.0, shape=(1,), dtype=np.float32),
                "IRS": Box(low=0.0, high=1.0, shape=(1,), dtype=np.float32)
            }
        )


    def _get_obs(self):
        return self.config_map.get_initial_state()
    
    def _get_info(self):
        return None # get the 


    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)

        observation = self._get_obs()
        info = self._get_info()

        return observation, info
    
    def step(self, action): # after one year of intervention get new intervention
        """
        TODO: 
        - take the action from the agent and write it to configuration files
        - run simulation using the configration 
        - use the output folder to get the reward and return to next step for observation by the agent
        """ 

        # An episode is done iff the agent has reached the target
        terminated = 0
        reward = 1 if terminated else 0  # Binary sparse rewards
        observation = self._get_obs()
        info = self._get_info()

        return observation, reward, terminated, False, info