'''
This is the implementation of thompson sampling to solve the problem of exploit-explore dilemma.
'''
import matplotlib.pyplot as plt
import numpy as np

from multi_bandit.bandit import Bandit


def run_thompson_sampling(true_means, n_pull):
    bandits = []
    for true_mean in true_means:
        bandits.append(Bandit(true_mean))

    rewards = []
    cumulative_average = []
    mean_rewards = 0

    for i in range(n_pull):
        # epsilon greedy
        p = np.random.random()
        if p < 1.0 / (i + 1):
            j = np.random.choice(len(bandits))
        else:
            j = np.argmax([b.sample_mean for b in bandits])

        reward = bandits[j].pull()
        rewards.append(reward)

        mean_rewards = 1 / (i + 1) * (mean_rewards * i + reward)
        _, average = thompson_sampling(i + 1, rewards, mean_rewards)
        cumulative_average.append(average)

    # cumulative_average = np.cumsum(rewards) / (np.arange(n_pull) + 1)
    return cumulative_average


def thompson_sampling(N, X, mean_0, precision=1, lambda_0=1):
    lambda_1 = lambda_0 + precision * N
    mean_1 = (mean_0 * lambda_0 + precision * np.sum(X)) / lambda_1
    return lambda_1, mean_1


if __name__ == '__main__':
    N = 50000

    cumulative_average1 = run_thompson_sampling(true_means=[1, 2, 3], n_pull=N)

    plt.plot(np.arange(start=0, stop=N, step=1), cumulative_average1)
    plt.xscale('log')
    plt.title('Thompson sampling')
    plt.xlabel('Iteration')
    plt.ylabel('sample mean')
    plt.show()
