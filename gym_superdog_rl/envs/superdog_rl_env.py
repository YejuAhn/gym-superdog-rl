import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_superdog_rl.envs.superdog_rl_world import WorldView


class SuperdogEnv(gym.Env):
    def __init__(self, enable_render = True):
        self.world_view = WorldView(world_name = "Adventure of Superdog")
        self.observation_space = spaces.Box(low=0, high=3, shape=(self.world_view.tile_height, self.world_view.tile_width))#




