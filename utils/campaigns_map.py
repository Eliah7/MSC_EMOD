from gym.spaces import Dict, Box
from utils.json_helper import JSONHelper

class CampaignsMap:
    """
    Map campaigns file to variables used by the environment
    """
    def __init__(self, env) -> None:
        self.env = env
        self.configs = JSONHelper("data/config.json")

    def write_actions(self, action):
        IRS_action = action['IRS'][0]
        ITNS_action = action['ITNS'][0]
        pass