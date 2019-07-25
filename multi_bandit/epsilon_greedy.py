'''
This is epsilon greedy implementation to solve the problem of exploit-explore dilemma.
'''
import matplotlib.pyplot as plt
import numpy as np

from multi_bandit.bandit import Bandit


def run_epsilon_greedy(true_means, epsilon, n_pull):
    bandits = []
    for true_mean in true_means:
        bandits.append(Bandit(true_mean))

    rewards = []

    for i in range(n_pull):
        # return a sample from uniform distribution, not gaussian distribution
        p = np.random.random()

        if p < epsilon:
            # explore: gather more information
            selected_bandit_idx = np.random.choice(len(bandits))
        else:
            # exploit: choose the best multi_bandit among bandits
            # most of the time, we exploit.
            selected_bandit_idx = np.argmax([bandit.sample_mean for bandit in bandits])

        rewards.append(bandits[selected_bandit_idx].pull())

    cumulative_average = np.cumsum(rewards) / (np.arange(n_pull) + 1)
    return cumulative_average


if __name__ == '__main__':
    N = 100000

    # try with different values of epsilon
    cumulative_average1 = run_epsilon_greedy(true_means=[1, 2, 3], epsilon=0.1, n_pull=N)
    cumulative_average2 = run_epsilon_greedy(true_means=[1, 2, 3], epsilon=0.05, n_pull=N)
    cumulative_average3 = run_epsilon_greedy(true_means=[1, 2, 3], epsilon=0.01, n_pull=N)

    plt.plot(np.arange(start=0, stop=N, step=1), cumulative_average1, label='epsilon=0.1')
    plt.plot(np.arange(start=0, stop=N, step=1), cumulative_average2, label='epsilon=0.05')
    plt.plot(np.arange(start=0, stop=N, step=1), cumulative_average3, label='epsilon=0.01')
    plt.xscale('log')
    plt.xlabel('Iteration')
    plt.ylabel('sample mean')
    plt.legend()
    plt.show()
