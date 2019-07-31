from grid_wind.board import Board
from grid_wind.policy_evaluation import Policy_Evaluation
from grid_wind.policy_improvement import Policy_Improvement

if __name__ == '__main__':
    b = Board()

    is_done = False

    iteration = 0
    while not is_done:
        print()
        iteration += 1
        print(f'iteration {iteration}')

        iter = Policy_Evaluation()
        iter.evaluate(b, discount_rate=0.9)
        print('Policy evaluation done... Current table of value functions')
        b.print_value_functions()

        impro = Policy_Improvement()
        policy_stable = impro.improve(b, discount_rate=0.9)
        print('Policy improvement done... Current table of actions')
        b.print_current_actions()

        if policy_stable:
            is_done = True

    print('\nThe final table of value functions')
    b.print_value_functions()

    print('\nThe final table of actions')
    b.print_current_actions()
    print(f'Start at state ({b.start_state})')
