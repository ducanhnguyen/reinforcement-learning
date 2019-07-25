'''
This is the implementation of upper confidence bound (ucb1) to solve the problem of exploit-explore dilemma.
'''
import matplotlib.pyplot as plt
import numpy as np

from multi_bandit.bandit import Bandit


def run_ucb1(true_means, n_pull):
    '''

    :param true_means:
    :param n_pull:
    :param upper_limit: The upper limit of true mean of bandits. Note that the true mean og bandits can not be large.
    :return:
    '''
    bandits = []
    for true_mean in true_means:
        bandits.append(Bandit(true_mean))

    rewards = []

    N = np.zeros(shape=(len(bandits)))

    for i in range(n_pull):
        # we always exploit: choose the best multi_bandit among bandits
        # choose the multi_bandit having the highest value of ucb1
        selected_bandit_idx = np.argmax([compute_ucb1(bandit, i + 1, N[idx]) for idx, bandit in enumerate(bandits)])
        N[selected_bandit_idx] += 1
        rewards.append(bandits[selected_bandit_idx].pull())

    cumulative_average = np.cumsum(rewards) / (np.arange(n_pull) + 1)
    return cumulative_average


def compute_ucb1(bandit, N, N_j):
    assert (N >= N_j and N_j >= 0)
    smoothing = 1e-10
    return bandit.sample_mean + np.sqrt(2 * np.log(N) / (N_j + smoothing))


if __name__ == '__main__':
    N = 100000

    cumulative_average1 = run_ucb1(true_means=[1, 2, 3], n_pull=N)

    plt.plot(np.arange(start=0, stop=N, step=1), cumulative_average1)
    plt.xscale('log')
    plt.title('UCB1')
    plt.xlabel('Iteration')
    plt.ylabel('sample mean')
    plt.show()
