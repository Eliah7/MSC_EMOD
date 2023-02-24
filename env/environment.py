import gym
from gym.spaces import Dict, Box, Tuple
import numpy as np
from utils.config_map import Configurations
from utils.campaigns_map import CampaignsMap


class MalariaEnvironment(gym.Env):
    def __init__(self, render_mode=None, size=5):
        super(MalariaEnvironment, self).__init__()
        self.config_map = Configurations(self)
        self.campaign_map = CampaignsMap(self)
        # Observations are dictionaries with the simulation configurations
        
        self.observation_space = Dict({
            "Acquisition_Blocking_Immunity_Decay_Rate": Box(low=0.0, high=1.0, shape=(1,), dtype=np.float32)
        })
        

        # self.observation_space = Box(low=-1.0, high=2.0, shape=(2, 1), dtype=np.float32)

        # We have 2 dimensions each bounded from (0,1] for itns and another irs
        # self.action_space =  Dict(  # coverage of ITNS and IRS
        #     {
        #         "ITNS": Box(low=0.0, high=1.0, shape=(1,), dtype=np.float32),
        #         "IRS": Box(low=0.0, high=1.0, shape=(1,), dtype=np.float32)
        #     }
        # )

        self.action_space = Box(low=0.0, high=1.0, shape=(1,), dtype=np.float32)


    def _get_obs(self):
        # print("INITIAL STATE", self.config_map.get_initial_state())
        
        return self.config_map.get_initial_state()
    
    def _get_info(self):
        return self._get_obs()

    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        # super().reset()

        observation = self._get_obs()
       
        info = self._get_info()
        # print(observation, info)

        return observation
    

    def step(self, action): # after one year of intervention get new intervention
        """
        TODO: 
        - take the action from the agent and write it to configuration files
        - run simulation using the configuration 
        - use the output folder to get the reward and return to next step for observation by the agent
        - after each action is executed copy the new state into the data dir and update the state
        """ 
        # take the actions and set them in the configurations
        # run the simulation
        # IRS_action = action['IRS'][0]
        # ITNS_action = action['ITNS'][0]

        # print(f"ACTIONS: IRS {IRS_action}; ITNS {ITNS_action}\n")

        # An episode is done iff the agent has reached the target
        terminated = 0
        reward = 1 if terminated else 0  # Binary sparse rewards
        observation = self._get_obs()
        # print(type(observation), observation)
        info = self._get_info()

        return observation, reward, False, observation