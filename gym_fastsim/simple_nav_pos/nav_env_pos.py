# import os, subprocess, time, signal
import numpy as np
# import gym
from gym import spaces
# from gym import utils
# from gym.utils import seeding
from gym_fastsim.simple_nav.nav_env import SimpleNavEnv
# import math
# import random
import logging

import pyfastsim as fs

logger = logging.getLogger(__name__)

class SimpleNavPosEnv(SimpleNavEnv):
        def __init__(self,xml_env, reward_func="binary_goalbased",render=False, light_sensor_range=200., light_sensor_mode="realistic", physical_traps=False):
                super().__init__(xml_env, reward_func=reward_func, render=render,
                                 light_sensor_range=light_sensor_range,
                                 light_sensor_mode=light_sensor_mode,
                                 physical_traps=physical_traps)
                
                self.observation_space = spaces.Box(low=np.array([0,0,-np.inf, -np.inf, -1, -1]), high=np.array([600,600,np.inf,np.inf,1,1], dtype=np.float32))
                self.action_space = spaces.Box(low=-self.maxVel, high=self.maxVel, shape=(2,), dtype=np.float32)
                ## [posx, posy, vx, vy, sin(or), cos(or)]
                self.state_dim = self.observation_space.shape[0] 
                
        def sample_q_vectors(self):
                ## Define environment limits
                ## (depends on loaded xml env, use self.map or self.xml_env):
                l_lims = [10, 10, -1, -1, -1, -1]
                h_lims = [590, 590, 1, 1, 1, 1]
                ## Sample state in BS
                s = np.random.uniform(low=l_lims, high=h_lims, size=(self.state_dim,))
                ## Create associated qpos and qvel (just for compatibility w/ mujoco)
                # qpos = s[:len(s)//2]; qvel = s[len(s)//2:]
                qpos = [*s[:2], *s[-2:]]; qvel = [*s[2:4]]
                return qpos, qvel, s

        def set_state(self, qpos, qvel):
                pos = [*qpos[:2], np.arctan2(qpos[-2],qpos[-1])]
                # if (np.array(pos) < 0).any():
                        # import pdb;pdb.set_trace()
                p = fs.Posture(*pos)
                self.robot.set_pos(p)
        
        def get_all_sensors(self):
                state = [0.]*6
                state[:2] = self.current_pos[:2]
                state[2:4] = [self.current_pos[i] - self.old_pos[i] for i in range(2)]
                a = self.current_pos[2]
                state[4:] = [np.sin(a), np.cos(a)]
                return state
