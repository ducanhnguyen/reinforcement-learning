import pandas as pd

from tic_tac_toe.board import Board
from tic_tac_toe.training import Training

import numpy as np
def play_with_machine(V_machine, human=Board.x_symbol, machine=Board.o_symbol):
    '''

    :param V: value functions of machine
    :param human: 'x' or 'o'
    :param machine: 'o' or 'x'
    :return:
    '''
    current_turn = human

    b = Board()
    board = b.board

    states = []
    states_reward = []

    while not b.is_game_over():

        if current_turn == human:
            print(f'>>> Human turn ({human})')
        else:
            print(f'>>> Machine turn ({machine})')

        if current_turn == human:
            # ask human for move
            available_move = False

            while not available_move:
                print('Let choose the cell you want to play (e.g., 1 2): ')
                inp = input().split(' ')

                row = int(inp[0])
                col = int(inp[1])

                if row > b.height or col > b.width or row < 0 or col < 0:
                    available_move = False
                    print('Wrong move!')
                elif board[row, col] == Board.empty_id:
                    board[row, col] = b.convert_turn_symbol2id(current_turn)
                    available_move = True
                else:
                    available_move = False
                    print('Wrong move!')

        else:
            # find potential moves
            potential_states = []
            potential_moves = []

            for i in range(b.height):
                for j in range(b.width):

                    if board[i, j] == b.empty_id:
                        board[i, j] = b.convert_turn_symbol2id(current_turn)

                        potential_states.append(b.get_state())
                        potential_moves.append([i, j])

                        board[i, j] = b.empty_id

            # find the best move
            if len(potential_moves) > 0:
                best_move_value = 0
                best_move = []
                #print(f'potential_moves = {potential_moves}')

                for idx, state in enumerate(potential_states):
                    print(f'potential move {potential_moves[idx]} = {np.round(V_machine[potential_states[idx]],2)}')

                for move, state in zip(potential_moves, potential_states):
                    if V_machine[state] > best_move_value:
                        best_move_value = V_machine[state]
                        best_move = move

                # play
                print(f'best move: {best_move}')
                board[int(best_move[0]), int(best_move[1])] = b.convert_turn_symbol2id(current_turn)

        # store the state of the board
        states.append(b.get_state())
        states_reward.append(Training.AVERAGE_REWARD)

        # change turn
        if current_turn == human:
            current_turn = machine
        else:
            current_turn = human

        b.draw_board()

    print(f'Winner = {b.winner_symbol}')

    #relearn()

'''
def relearn(new_states, new_winner):
    df_Vx = pd.read_csv('../tic_tac_toe/Vx.csv')
    Vx = df_Vx.to_numpy()

    df_Vo = pd.read_csv('../tic_tac_toe/Vo.csv')
    Vo = df_Vo.to_numpy()

    t = Training()
    if new_winner == Board.o_symbol:
        Vx = t.update_value_function(Vx, new_states)
        t.export_V(Vx, '../tic_tac_toe/Vx.csv')

        Vo = t.update_value_function(Vo, new_states)
        t.export_V(Vo, '../tic_tac_toe/Vo.csv')
'''

def convert_array2dict(V):
    '''

    :param V: Nx2 matrix, column 0 is the id of state, column 1 is the value function of the state
    :return:
    '''
    d = dict()

    for idx in range(len(V)):
        id = V[idx, 0]
        value = V[idx, 1]
        d[id] = value
    return d


if __name__ == '__main__':
    df_Vx = pd.read_csv('../tic_tac_toe/Vx.csv')
    Vx = df_Vx.to_numpy()
    Vx = convert_array2dict(Vx)

    df_Vo = pd.read_csv('../tic_tac_toe/Vo.csv')
    Vo = df_Vo.to_numpy()
    Vo = convert_array2dict(Vo)

    play_with_machine(Vo)
