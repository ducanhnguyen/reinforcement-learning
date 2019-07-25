# reinforcement-learning
exploit-explore dilemma solution, tic tac toe implementation, etc.

## Exploit-explore dilemma

*Multi-armed bandit problem*. is a problem in which a fixed limited set of resources must be allocated between competing (alternative) choices in a way that maximizes their expected gain, when each choice's properties are only partially known at the time of allocation, and may become better understood as time passes or by allocating resources to the choice. (wiki)

The problem of building an intelligent machine to play multi-armed bandit is the exploit-explore dilemma. There are some popular methods to solve the problem of exploit-explore dilemma such as epsilon greedy, upper confidence bound, optimistic initial value, and Thompson sampling.

I tried to implement these methods and test with 3 bandits. Bandit 1 has the true mean of 1. Bandit 2 has the true mean of 2. Bandit 3 has the true mean of 3. 

Rule: Player can choose any bandit to pull, then get a reward. Our objective is to maximize the sum of rewards.

The experiments are described along with method and as follows.

### Epsilon greedy

I tested with different values of epsilon, i.e. 0.1, 0.05 and 0.01. The comparison is shown in the figure below. As you can see, the experiment with epsilon = 0.1 converged fastest to the true mean value among the three experiments.

After 10^3 iterations, all of the experiments converge to around 3.0 which is the true mean.

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/epsilon_greedy_comparison.png" width="650">

### Upper confidence bound (ucb1)

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/ucb1.png" width="650">

### Optimistic initial value

The below figure shows the comparison among three configurations of optimistic initial value, i.e., upper limit = 10, 100, and 1000. The curve corresponding to upper_limit = 100 converges fastest to the true mean.

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/oit_comparison.png" width="650">

### Thompson sampling

#### Gaussian Thompson sampling

Gaussian Thompson sampling is used when we need to estimate the distribution of true mean given a set of observations from a gaussian distribution. The larger number of observations, the more exactly the estimation of the true mean is.

Experiment: true mean = 21, standard deviation = 10

- 10 observations: mean ~ N(14.452920733576656, 0.008333333333333333) (worse estimation)

- 10000 observations: mean ~ N(21.02135557402719, 8.333333333333334e-06) (better estimation)

#### Binary Thompson sampling

Binary Thompson sampling is used when we need to estimate the range of true mean given a set of observations from Bernoulli distribution. The range of true mean can be interpreted as the distribution of the true mean.

When we collect more observations, the range of true mean is thinner. You can see the difference in the distribution of true mean in the two figures below.

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/thompson_sampling_100_observations.png" width="650">

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/thompson_sampling_10_observations.png" width="650">

## Tic-tac-toe game

Tic-tac-toe is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game. (wiki)

*Terms*

| Name  | Corresponding term in reinforcement learning | 
| ------------- | ------------- |
| player, machine  |  agent (sense the environment and take action) | 
| board (3x3) | environment (where agent senses and takes action) |
| reward  | reward  |
| state | state (a configuration of the environment) |

*Algorithm*

Step 1: Train

- 1.1. Get all possible states of the board

- 1.2. Initialize value functions of states: the initial value maybe 0.5, 0 or 1 depended on the situation.

- 1.3. Play automatically under N times (N should be large) to update value functions. I use *temporal difference learning*.

Step 2: Play with machine

- Rule: Human plays first, the next turn is the machine.

- Strategy: Machine is not allowed to choose random empty cells (of course, because we are making an intelligent machine player). The strategy of the machine is to choose the best possible move from a set of possible moves. Here, each possible move will change the state of the board. We have known that each state of the board is associated with a value function. The higher value function of a state means that the state is better and worth playing.

*Experiment*

Human plays first (x). The machine is 'o' player.

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/tic_tac_toe.png" width="450">
