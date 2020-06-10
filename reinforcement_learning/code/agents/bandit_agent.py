import numpy as np

class Agent:
    def __init__(self, action_space, state_space, step_size=0., epsilon=0., e_greedy=False, ucb_const=0., ucb=False, optimal_initial_value=0., gradient=False):
        self.e_greedy = e_greedy
        self.ucb= ucb
        self.epsilon = epsilon
        self.gradient = gradient
        self.ucb_const = ucb_const
        self.state_space = state_space
        self.action_space = action_space
        self.action_idx = np.arange(action_space)
        self.step_size = step_size
        self.optimal_initial_value = optimal_initial_value
        self.reset()

    def reset(self):
        self.Q = np.zeros(self.action_space) + self.optimal_initial_value
        self.action_count = np.zeros(self.action_space)
        self.time_step = 0
        self.avg_reward = 0

    def act(self):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.action_idx)
        if self.e_greedy:
            best_action_value = np.max(self.Q)
            return np.random.choice(np.where(self.Q == best_action_value)[0])
        if self.ucb:
            ucb_estimation = self.Q + self.ucb_const*np.sqrt(np.log(self.time_step+1)/(self.action_count+1e-5))
            best_action_value = np.max(ucb_estimation)
            return np.random.choice(np.where(ucb_estimation == best_action_value)[0])
        if self.gradient:
            e = np.exp(self.Q)
            self.action_prob = e/np.sum(e)
            return np.random.choice(self.action_idx, p=self.action_prob)

    def step(self, action, reward, sample_average=False, use_baseline = False):
        self.action_count[action]+=1
        self.time_step += 1
        self.avg_reward += (reward-self.avg_reward)/self.time_step
        if sample_average:
            self.Q[action] += (reward - self.Q[action])/self.action_count[action]
        elif self.gradient:
            one_hot = np.zeros(self.action_space)
            one_hot[action]=1
            baseline = 0.
            if use_baseline:
                baseline = self.avg_reward
            self.Q += self.step_size*(reward-baseline)*(one_hot-self.action_prob)
        else:
            self.Q[action] += self.step_size*(reward - self.Q[action])
