"""
Use the configurations class to get and save data from the configuration files in which the simulation draws from.
"""
class Configurations:
    def __init__(self, env) -> None:
        self.env = env

    def get_initial_state(self):
        return self.env.observation_space.sample()
