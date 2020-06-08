import numpy as np

class Agent:
    def __init__(self, action_spce, state_space, seed = 0, epsilon=0., e_greedy=False, ucb_const=0., ucb=False):
        self.e_greedy = e_greedy
        self.ucb= ucb
        self.epsilon = epsilon
        self.ucb_const = ucb_const
        self.state_space = state_space
        self.action_space = action_space
        self.seed = seed
        self.reset()

    def reset(self):
        self.Q = np.zeros(self.action_space)
        self.action_count = np.zeros(self.action_space)
        self.step = 0
        np.random.seed(self.seed)

    def act(self):
        if np.random.rand() < self.epsilon:
            return np.random.choice(range(self.action_space))
        if self.e_greedy:
            best_action_value = np.argmax(self.Q)
            return np.random.choice(np.where(self.Q == best_action_value)[0])
        if self.ucb:
            # todo
            pass

    def step(self, action, reward, sample_average=False):
        self.action_count[action]+=1

        if sample_average:
            self.Q[action] += (reward - self.Q[action])/self.action_count[action]
