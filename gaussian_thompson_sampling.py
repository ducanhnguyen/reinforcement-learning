import matplotlib.pyplot as plt
import numpy as np


class GaussianThompsonSampling:
    def __init__(self):
        pass

    def fit(self, true_mean, N, sd, precision = 12):
        '''
        Find the distribution of true mean.
        :param true_mean: true mean
        :param N: the number of observations
        :param sd: standard deviation
        :param precision: inverse of variance
        :return: the distribution of true mean given the observations
        '''

        # generate samples following gaussian distribution
        # this is normal distribution with known precision τ
        samples = np.random.normal(loc=true_mean, scale=sd, size=N)

        # let find the distribution of true mean given the observations.
        # First, init lambda and sample mean
        variance_0 = 0
        sample_mean_0 = 0

        # update the distribution of sample mean
        # the formula of update can be found here: https://en.wikipedia.org/wiki/Conjugate_prior
        variance_1 = variance_0 + precision * N
        mean_1 = (sample_mean_0 * variance_0 + precision * np.sum(samples)) / (variance_0 + precision * N)

        print(f'sample mean ~ N({mean_1}, {1/variance_1})')


if __name__ == '__main__':
    sampling = GaussianThompsonSampling()
    sampling.fit(true_mean=21, N=10000, sd=10)
