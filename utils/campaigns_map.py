from gym.spaces import Dict, Box
from utils.json_helper import JSONHelper

class CampaignsMap:
    """
    Map campaigns file to variables used by the environment
    """
    def __init__(self, env) -> None:
        self.env = env
        self.configs = JSONHelper("data/campaign.json")

    def set_actions(self, action):
        IRS_action = action['IRS'][0]
        ITNS_action = action['ITNS'][0]

        print(f"Setting IRS to {IRS_action}")
        print(f"Setting ITNS to {ITNS_action}")


        self.configs.write_actions(IRS_action, ITNS_action)

        return True
    
    