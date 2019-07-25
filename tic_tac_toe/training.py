import csv

import numpy as np
import pandas as pd

from tic_tac_toe.board import Board


class Training:
    HIGHEST_REWARD = 1
    LOWEST_REWARD = 0
    AVERAGE_REWARD = 0.5

    def __init__(self):
        # store states
        self.states = set()

        # a pair = (state, game_over, winner)
        self.pairs = []

    def get_all_possible_states(self, b, turn_id):
        '''
        Get all possible states when playing on the board
        :param b: board
        :param turn_id: the id of the starting player
        :return:
        '''
        # when playing automatically, some moves make the board invalid
        # when the board is invalid, we no longer play
        if b.is_valid_board():
            state = b.get_state()

            if state not in self.states:
                # ignore duplicate states
                self.states.add(state)
                self.pairs.append([state, b.is_game_over(), b.get_winner()])

            if not b.is_game_over():

                for h in range(b.height):
                    for w in range(b.width):

                        if b.board[h, w] == Board.empty_id:
                            b.board[h, w] = turn_id

                            # change turn
                            if turn_id == Board.x_id:
                                turn_id = Board.o_id
                            elif turn_id == Board.o_id:
                                turn_id = Board.x_id

                            # switch to the next player
                            self.get_all_possible_states(b, turn_id)

                            # reset turn
                            if turn_id == Board.o_id:
                                turn_id = Board.x_id
                            elif turn_id == Board.x_id:
                                turn_id = Board.o_id

                            # reset the state
                            b.board[h, w] = Board.empty_id

    def initialize_Vx(self, pairs):
        '''
        Initialize value functions for 'x' player
        :param pairs: dataframe = (State_id, is_over, winner)+
        :return: a dictionary. key is the id of the state. value is the value function of that state.
        '''
        Vx = dict()

        for idx in range(len(pairs)):
            over = pairs.at[idx, 'is_over']
            winner = pairs.at[idx, 'winner']
            id = pairs.at[idx, 'State_id']

            if over:
                if winner == Board.x_symbol:
                    Vx[id] = self.HIGHEST_REWARD
                else:
                    Vx[id] = self.LOWEST_REWARD
            else:
                Vx[id] = self.AVERAGE_REWARD

        return Vx

    def initialize_Vo(self, pairs):
        '''
        Initialize value functions for 'o' player
        :param pairs: dataframe = (State_id, is_over, winner)+
        :return:
        '''
        Vo = dict()

        for idx in range(len(pairs)):
            over = pairs.at[idx, 'is_over']
            winner = pairs.at[idx, 'winner']
            id = pairs.at[idx, 'State_id']

            if over:
                if winner == Board.o_symbol:
                    # in case that the winner is 'o' player, the state is worth the highest reward
                    Vo[id] = self.HIGHEST_REWARD
                else:
                    # in case that the winner is 'x' player, the state is received the lowest reward
                    Vo[id] = self.LOWEST_REWARD
            else:
                # the game does not come to an end, every value function of the current state is equal to 0.5
                Vo[id] = self.AVERAGE_REWARD

        return Vo

    def find_possible_states(self, output_path, export=True):
        '''
        Get all possible states
        :param output_path:
        :param export:
        :return:
        '''
        b = Board()
        print('get all possible states: player x plays at first')
        self.get_all_possible_states(b, Board.x_id)

        print('get all possible states: player o plays at first')
        self.get_all_possible_states(b, Board.o_id)

        print(f'Num of possible states = {len(t.states)}')

        # export to file
        if export:
            print(f'export possible states to file')

            with open(output_path, mode='w') as employee_file:
                writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['State_id', 'is_over', 'winner'])

                WINNER_COLUMN = 2
                OVER_COLUMN = 1
                STATE_ID_COLUMN = 0

                for pair in self.pairs:
                    if pair[WINNER_COLUMN] == None:
                        # in case that the game is not ended, there is no winner
                        writer.writerow([pair[STATE_ID_COLUMN], pair[OVER_COLUMN], 'None'])
                    else:
                        writer.writerow(pair)

    def update_value_function(self, V, current_id_states, current_V, learning_rate=0.3):
        '''
        Update value functions of state
        :param V: dictionary of value function. key is id of state. value is the value function of the state.
        :param current_id_states: Nx1 array, where N is the number of states.
        :param learning_rate:
        :return:
        '''

        target = current_V[-1]

        for i in range(len(current_id_states) - 1, -1, -1):
            current_id = current_id_states[i]

            V[current_id] += learning_rate * (target - V[current_id])
            target = V[current_id]

        return V

    def play_to_train(self, Vo, Vx, n_iterations=10000, initial_player=Board.x_symbol):
        '''
        Train
        :param Vo: the value functions of player 'o' (is a dictionary).
                    Example: Vo[1000010000] = 0.35,
                    where 1000010000 is the id of the state,
                    0.35 is the value function of the state 1000010000.
        :param Vx: the value functions of player 'x' (is a dictionary)
        :param n_iterations: the number of times we play
        :return:
        '''
        assert (initial_player == Board.x_symbol or initial_player == Board.o_symbol)
        assert (len(Vx) == len(Vo))
        assert (n_iterations > 0)

        current_turn = initial_player

        for iteration in range(n_iterations):
            if iteration % 1000 == 0:
                print(f'iteration = {iteration}')

            b = Board()
            board = b.board

            current_Vx = []
            current_Vo = []
            current_id_states = []

            draw = False
            game_over = False

            while not draw and not game_over:
                # print('++++++++++++++++++++++++++++++')

                # retrieve all empty cells
                empty_cells = []
                for i in range(b.height):
                    for j in range(b.width):
                        if board[i, j] == 0:
                            empty_cells.append([i, j])
                # print(f'Empty cells = {empty_cells}')

                # just choose one empty cell to play
                if len(empty_cells) > 0:
                    played_cell = np.random.choice(len(empty_cells))
                    board[empty_cells[played_cell][0], empty_cells[played_cell][1]] = b.convert_turn_symbol2id(
                        current_turn)
                    # print(f'Play {current_turn} on {empty_cells[played_cell]}')

                    # update states
                    state = b.get_state()
                    current_id_states.append(state)

                    current_Vx.append(self.AVERAGE_REWARD)
                    current_Vo.append(self.AVERAGE_REWARD)

                    game_over = b.is_game_over()
                    # print(f'Over: {over}')
                    # print(f'Winner: {b.winner}')
                    # print(f'State id: {b.get_state()}')

                    # update turn
                    if current_turn == Board.x_symbol:
                        current_turn = Board.o_symbol
                    else:
                        current_turn = Board.x_symbol
                else:
                    draw = True

                # b.draw()

            # update the value function of states
            if game_over:
                winner = b.get_winner()

                if winner == Board.x_symbol:
                    current_Vx[-1] = self.HIGHEST_REWARD
                    current_Vo[-1] = self.LOWEST_REWARD
                elif winner == Board.o_symbol:
                    current_Vx[-1] = self.LOWEST_REWARD
                    current_Vo[-1] = self.HIGHEST_REWARD

                Vx = self.update_value_function(Vx, current_id_states, current_Vx)
                Vo = self.update_value_function(Vo, current_id_states, current_Vo)

            else:
                # print('Draw')
                pass

            # change the turn in the next play
            # 50% the game starts with the player 1
            # 50% the game starts with the player 2
            if current_turn == Board.x_symbol:
                current_turn = Board.o_symbol
            else:
                current_turn = Board.x_symbol

    def export_V(self, V, path):
        '''
        Export value functions of state to file
        :param V: the value function, is a dictionary.
                Example: Vo[1000010000] = 0.35,
                where 1000010000 is the id of the state,
                0.35 is the value function of the state 1000010000.
        :param path:
        :return:
        '''
        with open(path, mode='w') as employee_file:
            writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['State_id', 'value'])

            for item in V.items():
                writer.writerow(item)


if __name__ == '__main__':
    t = Training()

    # step 1: Find all possible states
    t.find_possible_states(output_path='../tic_tac_toe/pairs.csv')

    # step 2: initialize value functions of states for Vx and Vy
    pairs = pd.read_csv('../tic_tac_toe/pairs.csv')

    Vx = t.initialize_Vx(pairs)
    Vo = t.initialize_Vo(pairs)

    # step 3: play to update value functions
    t.play_to_train(Vo, Vx, n_iterations=100000)
    t.export_V(Vo, '../tic_tac_toe/Vo.csv')
    t.export_V(Vx, '../tic_tac_toe/Vx.csv')
