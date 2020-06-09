# inspired by
# 1- https://github.com/ShangtongZhang
# 2- https://github.com/JKCooper2/gym-bandits/blob/master/gym_bandits/bandit.py
import numpy as np
import gym
from gym import spaces
from gym.utils import seeding

class BanditEnv(gym.Env):
    def __init__(self, num_arms):
        self.num_arms = num_arms
        self.state_space = spaces.Discrete(1)
        self.action_space = spaces.Discrete(num_arms)
        self.reward_distribution = None

    def reset(self):
        self.reward_distribution = np.random.randn(self.num_arms)
        self.best_action = np.argmax(self.reward_distribution)

    def step(self, action):
        reward = self.reward_distribution[action] + np.random.randn()
        done = True
        info = None

        return 0, reward, done, info
