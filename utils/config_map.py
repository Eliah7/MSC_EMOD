from utils.json_helper import JSONHelper
from gym.spaces import Dict
from collections import OrderedDict
import numpy as np
from typing import OrderedDict
import gym 

class Configurations:
    """
    Use the configurations class to get and save data from the configuration files in which the simulation draws from.
    """
    def __init__(self, env) -> None:
        self.env = env
        self.configs = JSONHelper("data/config.json").json_obj['parameters']

    def get_initial_state(self) -> OrderedDict:
        return OrderedDict([
            ('Acquisition_Blocking_Immunity_Decay_Rate', np.array([self.configs['Acquisition_Blocking_Immunity_Decay_Rate']], dtype=np.float32))
        ])
       
        