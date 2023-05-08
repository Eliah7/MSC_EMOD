import gym
from gym.spaces import Dict, Box, Tuple
import numpy as np
from utils.config_map import Configurations
from utils.campaigns_map import CampaignsMap
from utils.output_map import OutputMap
from utils.simulation import run_simulation

class MalariaEnvironment(gym.Env):
    def __init__(self, render_mode=None, size=5):
        super(MalariaEnvironment, self).__init__()
        self.config_map = Configurations(self)
        self.campaign_map = CampaignsMap(self)
        self.output_map = OutputMap(self)
        # Observations are dictionaries with the simulation configurations
        
        self.observation_space = Dict({
            "Acquisition_Blocking_Immunity_Decay_Rate": Box(low=0.0, high=1.0, shape=(1,), dtype=np.float32)
        })
        
        # We have 2 dimensions each bounded from (0,1] for itns and another irs
        self.action_space =  Dict(  # coverage of ITNS and IRS
            {
                "ITNS": Box(low=0.0, high=1.0, shape=(1,), dtype=np.float32),
                "IRS": Box(low=0.0, high=1.0, shape=(1,), dtype=np.float32)
            }
        )


    def _get_obs(self):
        # print("INITIAL STATE", self.config_map.get_initial_state())
        return self.config_map.get_initial_state()
    
    def _get_info(self):
        return self._get_obs()

    def reset(self, seed=None, options=None):
        observation = self._get_obs()

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
    
        print(f"ACTION {action}")
        actions_set_ = self.campaign_map.set_actions(action)
        print(f"Action is set{actions_set_}")
        wait_for_sim = run_simulation()
        print(wait_for_sim)
        reward = self.output_map.get_rewards()
        print(f"REWARD {reward}")
        terminated = 0
        # reward = 1 if terminated else 0  # Binary sparse rewards
        observation = self._get_obs()
        done = True # environment is MAB

        return observation, reward, done, observation