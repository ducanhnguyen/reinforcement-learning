'''
Compare different algorithms to solve the problem of exploit-explore dilemma
'''
import matplotlib.pyplot as plt
import numpy as np

from multi_bandit.epsilon_greedy import run_epsilon_greedy
from multi_bandit.optimistic_initial_value import run_oit
from multi_bandit.thompsom_sampling import run_thompson_sampling
from multi_bandit.ucb1 import run_ucb1

if __name__ == '__main__':
    N = 50000

    thompson_sampling = run_thompson_sampling(true_means=[1, 2, 3], n_pull=N)
    epsilon_greedy = run_epsilon_greedy(true_means=[1, 2, 3], n_pull=N, epsilon=0.01)
    oit = run_oit(true_means=[1, 2, 3], n_pull=N)
    ucb1 = run_ucb1(true_means=[1, 2, 3], n_pull=N)

    iterations = np.arange(start=0, stop=N, step=1)
    plt.plot(iterations, thompson_sampling, label='thompson sampling')
    plt.plot(iterations, epsilon_greedy, label='epsilon greedy (epsilon=0.01)')
    plt.plot(iterations, oit, label='optimistic initial value')
    plt.plot(iterations, ucb1, label='ucb')
    plt.xscale('log')
    plt.title('Exploit-explore method comparisons')
    plt.xlabel('Iteration')
    plt.ylabel('sample mean')
    plt.legend()
    plt.show()
