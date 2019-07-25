import numpy as np


class Bandit:
    '''
    A multi_bandit is a game machine
    '''

    def __init__(self, true_mean):
        self.true_mean = true_mean
        self.sample_mean = 0
        self.N = 0

    def pull(self):
        '''
        When we pull from a multi_bandit, the multi_bandit will return a number.
        :return:
        '''
        # return a sample from gaussian normal distribution
        # the sample can not be sampled from uniform distribution
        reward = np.random.randn() + self.true_mean
        self.sample_mean = 1 / (self.N + 1) * (self.sample_mean * self.N + reward)
        self.N += 1
        return reward
