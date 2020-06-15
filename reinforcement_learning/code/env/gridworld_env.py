
import numpy as np
import gym
from gym import spaces
from gym.utils import seeding

class GridWorldEnv(gym.Env):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.action_space = [np.asarray([0, 1]),
                             np.asarray([1, 0]),
                             np.asarray([0, -1]),
                             np.asarray([-1, 0])]
        self.state_A = [0,1]
        self.state_A_prime = [4,1]
        self.state_B = [0,3]
        self.state_B_prime = [2,3]
        
    def step(self, action, state):
        if state == self.state_A:
            next_state = self.state_A_prime
            reward = 10
        elif state == self.state_B:
            next_state = self.state_B_prime
            reward = 5
        else:
            next_state = list(np.asarray(state) + action)
            if 0<=next_state[0]<self.w and 0<=next_state[1]<self.h:
                reward = 0
            else:
                next_state = state
                reward = -1
        return next_state, reward