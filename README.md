# reinforcement-learning
exploit-explore dilemma solution, tic tac toe implementation, etc.

## Exploit-explore dilemma



### Epsilon greedy

I tested with different values of epsilon, i.e. 0.1, 0.05 and 0.01. The comparison is shown in the figure below. As you can see, the experiment with epsilon = 0.1 converged fastest to the true mean value among three experiments.

After 10^3 iterations, all of experiments converge to around 3.0 which is true mean.

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/epsilon_greedy_comparison.png" width="650">

### Upper confidence bound (ucb1)

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/ucb1.png" width="650">

### Optimistic initial value

The below figure shows the comparison among three configuration of optimistic initial value, i.e., upper limit = 10, 100, and 1000. The curve corresponding to upper_limit = 100 converges fastest to true mean.

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/oit_comparison.png" width="650">

### Thompson sampling

#### Gaussian thompson sampling

Gaussian thompson sampling is used when we need to estimate the distribution of true mean given a number of observation from gaussian distribution. The more number of observations, the more exactly the estimation of true mean is.

Experiment: true mean = 21, standard deviation = 10

- 10 observations: mean ~ N(14.452920733576656, 0.008333333333333333) (worse estimation)

- 10000 observations: mean ~ N(21.02135557402719, 8.333333333333334e-06) (better estimation)

#### Binary thompson sampling

Binary thompson sampling is used when we need to estimate the range of true mean given a number of observations from bernoulli distribution. The range of true mean can be interpreted as the distribution of true mean.

When we collect more number of observations, the range of true mean is thinner. You can see the difference in the distribution of true mean in the two figures below.

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/thompson_sampling_100_observations.png" width="650">

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/thompson_sampling_10_observations.png" width="650">

## Tic-tac-toe game

Step 1: Train
- 1.1. Get all possible states
- 1.2. Initialize value functions of states
- 1.3. Play automatically under N times (N should be large) to update value functions.

Step 2: Play
- Rule: Human plays first, the next turn is machine.
- Strategy: Machine is not allowed to choose random empty cell (of course, because we are making an intelligent machine player). The strategy of machine is to choose a set of possible moves. Each possible move will change the state of board. We have known that each state of the board is associated to a value function. The higher value function of a state means that that state is better and worth playing.

Experiment

