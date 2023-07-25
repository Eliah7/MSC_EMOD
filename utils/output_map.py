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
        self.configs = JSONHelper("data/output/InsetChart.json").json_obj
        daily_infection_rate = np.array(self.configs["Channels"]["Daily (Human) Infection Rate"]["Data"])
        daily_eir = np.array(self.configs["Channels"]["Daily EIR"]["Data"])
        daily_disease_deaths = np.array(self.configs["Channels"]["Disease Deaths"]["Data"])
        infected = np.array(self.configs["Channels"]["New Infections"]["Data"])
        severe = np.array(self.configs["Channels"]["New Severe Cases"]["Data"])
        cost = np.array(self.configs["Channels"]["Campaign Cost"]["Data"])
        mean_parasitemia = np.array(self.configs["Channels"]["Mean Parasitemia"]["Data"])
        print(f"""
            Infected => {np.mean(infected)} 
            Severe Cases => {np.mean(severe)}
            Cost => {cost[len(cost)-1]/100000}
            Mean Parasitemia => {np.mean(mean_parasitemia)}
            Disease Deaths => {np.mean(daily_disease_deaths)}
        """)

        # return -np.mean(daily_infection_rate) + -np.mean(daily_eir) + -np.sum(daily_disease_deaths)
        return -np.mean(infected)/100 - np.mean(severe)/100 -  cost[len(cost)-1]/100000 #- np.mean(mean_parasitemia)/1000
        
    
    