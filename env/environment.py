import gym
from gym import spaces, Dict, Box
import numpy as np
from utils.config import Configurations
from utils.campaigns_map import CampaignsMap


class MalariaEnvironment(gym.Env):
    def __init__(self, render_mode=None, size=5):
        self.config_map = Configurations()
        self.campaign_map = CampaignsMap()
        # Observations are dictionaries with the simulation configurations
        """
        "gambiae": {
          "Acquire_Modifier": 1,
          "Adult_Life_Expectancy": 10,
          "Anthropophily": 0.95,
          "Aquatic_Arrhenius_1": 84200000000,
          "Aquatic_Arrhenius_2": 8328,
          "Aquatic_Mortality_Rate": 0.1,
          "Days_Between_Feeds": 3,
          "Egg_Batch_Size": 100,
          "Immature_Duration": 2,
          "Indoor_Feeding_Fraction": 1,
          "Infected_Arrhenius_1": 117000000000,
          "Infected_Arrhenius_2": 8336,
          "Infected_Egg_Batch_Factor": 0.8,
          "Infectious_Human_Feed_Mortality_Factor": 1.5,
          "Larval_Habitat_Types": {
            "TEMPORARY_RAINFALL": 1250000000
          },
          "Nighttime_Feeding_Fraction": 1.0,
          "Transmission_Rate": 0.5
        }
        """
        self.observation_space = Dict({"Transmission_Rate": Box(low=0.0, high=1.0, shape=(1,), dtype=np.float32)})

        # We have 2 dimensions each bounded from (0,1] for itns and another irs
        self.action_space = Dict()


    def _get_obs(self):
        return None # get the initial state
    
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
        terminated = np.array_equal(self._agent_location, self._target_location)
        reward = 1 if terminated else 0  # Binary sparse rewards
        observation = self._get_obs()
        info = self._get_info()

        return observation, reward, terminated, False, info