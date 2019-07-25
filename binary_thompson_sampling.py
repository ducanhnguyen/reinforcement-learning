'''
Raw implementation of thompson sampling for binary observation.

This example tries to estimate the distribution of mean from a set of binary observations.
'''
import matplotlib.pyplot as plt
import numpy as np


class BinaryThompsonSampling:
    def __init__(self):
        pass

    def posterior(self, theta, a, b, n_success, n_fail):
        a2 = a - 1 + n_success
        b2 = b - 1 + n_fail
        return theta ** a2 * (1 - theta) ** b2

    def fit(self, true_mean, N, a=1, b=1):
        '''
        We try to find the distribution of true mean of observations. Each observation return 0 or 1.
        We can think an observation as when we toss a coin.
        :param true_mean: the true mean
        :param N: then number of observations
        :param a: fixed to 1
        :param b: fixed to 1
        :return: sample mean
        '''
        # given true mean, let create a set of binary observations
        n_success = np.random.binomial(n=N, p=true_mean, size=1)
        print(f'n_success of {N} samples: {n_success}')

        # given a set of binary observations (we do not know true mean).
        # let use thompson sampling to find the distribution of true mean.
        # we will test with 100 possible values of theta
        # here, theta stands for sample mean
        theta_values = np.arange(100) / 100

        posteriors = []
        for theta_value in theta_values:
            # for each value of theta, we compute a value in terms of importance
            # the theta associated with higher value is more likely to be close to the true mean
            posterior = self.posterior(theta_value, a, b, n_success, N - n_success)
            posteriors.append(posterior)

        sample_mean = theta_values[np.argmax(posteriors)]

        # just for ytesting
        plt.plot(theta_values, posteriors)
        plt.title(f'true mean = {true_mean}\nsample mean ~ {sample_mean}, # observations = {N}')
        plt.xlabel('sample mean [0..1]')
        plt.ylabel('value')
        plt.show()


if __name__ == '__main__':
    sampling = BinaryThompsonSampling()
    sampling.fit(true_mean=0.8, N=100)
