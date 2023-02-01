from gym.spaces import Dict, Box

class CampaignsMap:
    """
    Map campaigns file to variables used by the environment
    """
    def __init__(self, env) -> None:
        self.env = env

    def get_initial_state(self):
        return self.env.observation_space.sample()
        # get the initial state if the episode is the first else get from the current file edited