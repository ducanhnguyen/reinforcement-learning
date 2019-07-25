'''
This is the implementation of optimistic initial value to solve the problem of exploit-explore dilemma.
'''
import matplotlib.pyplot as plt
import numpy as np

from multi_bandit.bandit import Bandit


def run_oit(true_means, n_pull, upper_limit=10):
    '''

    :param true_means:
    :param n_pull:
    :param upper_limit: The upper limit of true mean of bandits. Note that the true mean og bandits can not be large.
    :return:
    '''
    bandits = []
    for true_mean in true_means:
        bandit = Bandit(true_mean)
        bandit.sample_mean = upper_limit
        bandits.append(bandit)

    rewards = []

    for i in range(n_pull):
        # we always exploit: choose the best multi_bandit among bandits
        selected_bandit_idx = np.argmax([bandit.sample_mean for bandit in bandits])
        rewards.append(bandits[selected_bandit_idx].pull())

    cumulative_average = np.cumsum(rewards) / (np.arange(n_pull) + 1)
    return cumulative_average


if __name__ == '__main__':
    N = 100000

    cumulative_average1 = run_oit(true_means=[1, 2, 3], n_pull=N)

    plt.plot(np.arange(start=0, stop=N, step=1), cumulative_average1)
    plt.xscale('log')
    plt.title('Optimistic initial value')
    plt.xlabel('Iteration')
    plt.ylabel('sample mean')
    plt.show()
