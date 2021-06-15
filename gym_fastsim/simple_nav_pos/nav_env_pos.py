import os, subprocess, time, signal
import numpy as np
import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding
from gym_fastsim.simple_nav.nav_env import SimpleNavEnv
import math
import random
import logging

import pyfastsim as fs

logger = logging.getLogger(__name__)

class SimpleNavPosEnv(SimpleNavEnv):
        
        def __init__(self,xml_env, reward_func="binary_goalbased",render=False, light_sensor_range=200., light_sensor_mode="realistic"):
                super().__init__(xml_env)
                self.observation_space = spaces.Box(low=np.array([0,0,-2*np.pi]), high=np.array([600,600,2*np.pi], dtype=np.float32))
                self.action_space = spaces.Box(low=-self.maxVel, high=self.maxVel, shape=(2,), dtype=np.float32)

        def get_all_sensors(self):
                return self.current_pos
