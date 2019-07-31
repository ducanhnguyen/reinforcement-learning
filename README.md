# reinforcement-learning
exploit-explore dilemma solution, tic tac toe implementation, grid-world implementation, etc.

## 1. Exploit-explore dilemma

*Multi-armed bandit problem*. is a problem in which a fixed limited set of resources must be allocated between competing (alternative) choices in a way that maximizes their expected gain, when each choice's properties are only partially known at the time of allocation, and may become better understood as time passes or by allocating resources to the choice. (wiki)

The problem of building an intelligent machine to play multi-armed bandit is the exploit-explore dilemma. There are some popular methods to solve the problem of exploit-explore dilemma such as epsilon greedy, upper confidence bound, optimistic initial value, and Thompson sampling.

I tried to implement these methods and tested with 3 bandits. Bandit 1 has the true mean of 1. Bandit 2 has the true mean of 2. Bandit 3 has the true mean of 3. 

Rule: Player can choose any bandit to pull, then get a reward. Our objective is to maximize the sum of rewards.

The experiments are described along with method and as follows.

### 1.1. Epsilon greedy

I tested with different values of epsilon, i.e. 0.1, 0.05 and 0.01. The comparison is shown in the figure below. As you can see, the experiment with epsilon = 0.1 converged fastest to the true mean value among the three experiments.

After 10^3 iterations, all of the experiments converge to around 3.0 which is the true mean.

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/epsilon_greedy_comparison.png" width="650">

### 1.2. Upper confidence bound (ucb1)

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/ucb1.png" width="650">

### 1.3. Optimistic initial value

The below figure shows the comparison among three configurations of optimistic initial value, i.e., upper limit = 10, 100, and 1000. The curve corresponding to upper_limit = 100 converges fastest to the true mean.

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/oit_comparison.png" width="650">

### 1.4. Thompson sampling

#### 1.4.1. Gaussian Thompson sampling

Gaussian Thompson sampling is used when we need to estimate the distribution of true mean given a set of observations drawn from a gaussian distribution. The larger number of observations, the more exactly the estimation of the true mean is.

The figure below is the result when solving the multi-armed bandit problem.

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/thompson_sampling_arm.png"  width="650">

*Another experiment*: Assume we know that true mean = 21, standard deviation = 10. We will draw samples from this distribution, then use Thompson sampling to infer the distribution of true mean.

- With 10 observations: mean ~ N(14.452920733576656, 0.008333333333333333) (worse estimation)

- With 10000 observations: mean ~ N(21.02135557402719, 8.333333333333334e-06) (better estimation)

#### 1.4.2. Binary Thompson sampling

Binary Thompson sampling is used when we need to estimate the range of true mean given a set of observations drawn from  a Bernoulli distribution. The range of true mean can be interpreted as the distribution of the true mean.

When we collect more observations, the distribution of true mean is thinner. 


*Experiment*. This experiment is not related to the problem of multi-armed bandit. This just aims to help you understand more about binary thompson sampling. Let notice the difference of the distribution of true mean in the two figures below to see the importance of the number of observations.

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/thompson_sampling_100_observations.png" width="650">

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/thompson_sampling_10_observations.png" width="650">

#### Summary 

The summary of all methods to solve the problem of expolit-explore dilemma is as follows.

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/multi_bandit_comparison.png" width="650">

## 2. Tic-tac-toe game

Tic-tac-toe is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game. (wiki)

*Terms*

| Name  | Corresponding term in reinforcement learning | 
| ------------- | ------------- |
| player, machine  |  agent (sense the environment and take action) | 
| board (3x3) | environment (where agent senses and takes action) |
| reward  | reward  |
| state | state (a configuration of the environment) |

### 2.1. Algorithm

Step 1: Train

- 1.1. Get all possible states of the board

- 1.2. Initialize value functions of states: the initial value maybe 0.5, 0 or 1 depended on the situation.

- 1.3. Play automatically under N times (N should be large) to update value functions. I use *temporal difference learning*.

Step 2: Play with machine

- Rule: Human plays first, the next turn is the machine.

- Strategy: Machine is not allowed to choose random empty cells (of course, because we are making an intelligent machine player). The strategy of the machine is to choose the best possible move from a set of possible moves. Here, each possible move will change the state of the board. We have known that each state of the board is associated with a value function. The higher value function of a state means that the state is better and worth playing.

### 2.2. Experiment

The order is from the left to the right, from above to below.
Human plays first (x). The machine is 'o' player. Finally, the machine wins.

You can realize that the machine is not extremely intelligent. The main reason is that in the training phase, we play tic-tac-toe randomly without any human knowledge.

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/tic_tac_toe.png" width="450">

The result of this match will be used to train again. That is the meaning of the word 'reinforcement learning'. When we play more, the machine will be more intelligent.

## 3. Grid-world game

Grid-world is a MxN board. You act as an player starting at a cell on the board. You must go through cells to collect rewards and avoid obstacles with the least movements and the highest number of rewards.

Method: Use reinforcement learning

Here is an example of grid-world

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/gird_world_example.png" width="450">

### Algorithm of reinforcement learning

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/policy_iteration.png" width="650">

The algorithm I have used is described below. It is an iterative algorithm (chapter 4.3, page 97, book Reinforcement Learning: An Introduction - Richard S. Sutton and Andrew G. Barto). Each iteration of the algorithm is composed of two steps:

- Step 1. (Policy evaluation or iterative policy iteration): Given a policy, let find the value function V(s)

- Step 2. (Policy improvement): Change the current policy of a state to a better policy.

The algorithm terminates when there is no better policy.

### Experiment

I tried to create a 4x4 grid-world in which there are one positive reward (+1), one negative reward (-1), and one obstacle denoted by 'x').

The player starts at the state (3, 0). The players must avoid obstacles, eat positive reward, and ignore negative reward.

Initially, there is no action on the table of actions. After 15 iterations of the above algorithm, the best policy has been found.

*Iteration 1*

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/policy_iteration_1.png" width="450">

*Iteration 2*

Let see the different from this iteration with iteration 1. An action of a state has been changed.

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/policy_iteration_2.png" width="450">

*Iteration 15 (the last iteration)*

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/policy_iteration_15.png" width="450">

*The final result*

Table of actions

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/policy_iteration_actions.png" width="170">

Table of value functions

<img src="https://github.com/ducanhnguyen/reinforcement-learning/blob/master/img/policy_iteration_value_function.png" width="190">

Let try yourself with the above result. Remember that player will start at the state (3, 0). Move towards the direction defined in the table of action.
