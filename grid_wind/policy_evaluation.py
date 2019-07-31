'''
Given a policy, find V(s) of all states
'''
import numpy as np

from grid_wind.board import Board


class Policy_Evaluation:
    def __init__(self):
        pass

    def evaluate(self, board, discount_rate=0.9, converged_threshold=1e-3):
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
                        current_action = board.current_actions[i, j]

                        new_v = 0

                        # compute new value function
                        board.move(current_action)
                        next_state = board.current_state

                        new_v += (board.get_current_reward() + discount_rate * board.V[next_state[0], next_state[1]])
                        board.unmove(current_action)

                        board.V[i, j] = new_v

                        # compute delta
                        delta = np.abs(new_v - old_v)

                        if delta > max_delta:
                            max_delta = delta

            if max_delta <= converged_threshold:
                converged = True

            #print(f'[iterative policy evaluation] Iteration {iteration}: max_delta = {max_delta}')
            iteration += 1


if __name__ == '__main__':
    b = Board()

    print('Initial value function')
    b.print_value_functions()

    print('Initial actions')
    b.print_current_actions()

    print('Run iterative policy evaluation')
    iter = Policy_Evaluation()
    iter.evaluate(b)

    print('The final board')
    b.print_value_functions()
    print(f'Start at ({b.start_state})')
