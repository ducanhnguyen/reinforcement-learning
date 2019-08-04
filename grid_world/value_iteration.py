'''
Find the optimal policy.

Method: Value iteration
'''
import numpy as np

from grid_world.board import Board


class Value_Iteration:
    def __init__(self):
        pass

    def iterate(self, board, discount_rate=0.9, converged_threshold=1e-3):
        converged = False
        iteration = 0

        while not converged:

            max_delta = 0
            for i in range(board.height):
                for j in range(board.width):
                    if not board.terminal_states[i, j] and not board.obstables[i, j]:

                        # set the current state
                        board.current_state = [i, j]

                        old_v = board.V[i, j]
                        the_best_action = board.current_actions[i, j]
                        max_value_function = 0

                        # Because we assume that each state only has one possible action, pi(a|s) = 1 (we can ignore it)
                        # Also, because we only get a fixed state s' and reward r(a, a, s') from state s and action s, p(s', r(s, a, s') | a,s) = 1  (we can ignore it)
                        # (where s' is the next state, a: action, s: the current state)
                        # The final formula: V(s) = r(a, s, s') + discount_rate * V(s')
                        for possible_action in board.get_possible_actions_of_a_state(i, j):
                            # compute new value function
                            board.move(possible_action)
                            next_state = board.current_state

                            new_v = board.get_current_reward() + discount_rate * board.V[next_state[0], next_state[1]]

                            # store the action having the largest value function
                            if new_v > max_value_function:
                                max_value_function = new_v
                                the_best_action = possible_action

                            board.unmove(possible_action)

                        # update the new state of the board
                        board.move(the_best_action)

                        board.V[i, j] = max_value_function

                        # compute delta
                        delta = np.abs(max_value_function - old_v)

                        if delta > max_delta:
                            max_delta = delta

            if max_delta <= converged_threshold:
                converged = True

            print(f'[value iteration] Iteration {iteration}: max_delta = {max_delta}')
            iteration += 1


if __name__ == '__main__':
    b = Board()

    print('Initial value function')
    b.print_value_functions()

    print('Initial actions')
    b.print_current_actions()

    print('Run iterative policy evaluation')
    iter = Value_Iteration()
    iter.iterate(b)

    print('The final board')
    b.print_value_functions()
    print(f'Start at ({b.start_state})')
