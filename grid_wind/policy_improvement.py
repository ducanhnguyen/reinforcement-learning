class Policy_Improvement:
    def __init__(self):
        pass

    def improve(self, board, discount_rate=0.9):
        policy_stable = True

        for i in range(board.height):
            for j in range(board.width):
                if not board.obstables[i, j]:
                    board.current_state = [i, j]
                    V_old = board.V[i, j]
                    current_action = board.current_actions[i, j]

                    best_action = current_action
                    for possible_action in board.get_possible_actions_of_a_state(i, j):
                        if possible_action != current_action:

                            board.move(possible_action)
                            # now, the current state is the next state
                            next_state = board.current_state
                            V_new = board.get_current_reward() + discount_rate * board.V[
                                next_state[0], next_state[1]]
                            board.unmove(possible_action)

                            if V_new > V_old:
                                policy_stable = False
                                best_action = possible_action
                                V_old = V_new

                    # update action
                    if current_action!=best_action:
                        board.current_actions[i, j] = best_action

                    if not policy_stable:
                        break

            if not policy_stable:
                break

        return policy_stable
