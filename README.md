# reinforcement-learning
exploit-explore dilemma solution, tic tac toe implementation, etc.

## Exploit-explore dilemma



### Epsilon greedy

I tested with different values of epsilon, i.e. 0.1, 0.05 and 0.01. The comparison is shown in the figure below. As you can see, the experiment with epsilon = 0.1 converged fastest to the true mean value among three experiments.

After 10^3 iterations, all of experiments converge to around 3.0 which is true mean value.

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/epsilon_greedy_comparison.png" width="650">

### Upper confidence bound (ucb1)



### Optimistic initial value

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/oit_comparison_1.png" width="650">

### Thompson sampling

#### Gaussian thompson sampling

10 observations: sample mean ~ N(14.452920733576656, 0.008333333333333333)

10000 observations: sample mean ~ N(21.02135557402719, 8.333333333333334e-06)

#### Binary thompson sampling

