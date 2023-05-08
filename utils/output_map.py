from gym.spaces import Dict, Box
from utils.json_helper import JSONHelper
import numpy as np

class OutputMap:
    """
    Map campaigns file to variables used by the environment
    """
    def __init__(self, env) -> None:
        self.env = env
        self.configs = JSONHelper("data/output/InsetChart.json").json_obj

    def get_rewards(self):
        # print(self.configs)
        daily_infection_rate = np.array(self.configs["Channels"]["Daily (Human) Infection Rate"]["Data"])
        daily_eir = np.array(self.configs["Channels"]["Daily EIR"]["Data"])
        daily_disease_deaths = np.array(self.configs["Channels"]["Disease Deaths"]["Data"])
        return -np.mean(daily_infection_rate) + -np.mean(daily_eir) + -np.sum(daily_disease_deaths)
        
    
    