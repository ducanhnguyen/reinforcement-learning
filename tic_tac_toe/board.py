import numpy as np


class Board:
    x_id = 1
    o_id = 5
    empty_id = 0

    x_symbol = 'x'
    o_symbol = 'o'
    empty_symbol = ' '

    def __init__(self, width=3, height=3):
        self.width = width
        self.height = height
        self.board = np.zeros(shape=(self.width, self.height))



        # in case of no winner, winner is None. Otherwise, winner is x or o.
        self.winner_symbol = None
        self.draw = False

    def convert_turn_symbol2id(self, turn_id):
        if turn_id == self.x_symbol:
            return self.x_id
        elif turn_id == self.o_symbol:
            return self.o_id

    def is_valid_board(self):
        x_count = np.sum([self.board == self.x_id])
        o_count = np.sum([self.board == self.o_id])
        diff = np.abs(x_count - o_count)

        if diff == 1 or diff == 0:
            return True
        else:
            return False

    def is_game_over(self):
        winner = None

        # three x (or o) in the row or column or diagonal line
        NUM_SYMBOL_TO_WIN = 3

        # check column
        for w in range(self.width):
            sum = 0

            for h in range(self.height):
                sum += self.board[h, w]

            if sum == self.o_id * NUM_SYMBOL_TO_WIN:
                winner = self.o_symbol
                break
            elif sum == self.x_id * NUM_SYMBOL_TO_WIN:
                winner = self.x_symbol
                break

        if winner == None:
            # check row
            for h in range(self.height):

                sum = 0
                for w in range(self.width):
                    sum += self.board[h, w]

                if sum == self.o_id * NUM_SYMBOL_TO_WIN:
                    winner = self.o_symbol
                    break
                elif sum == self.x_id * NUM_SYMBOL_TO_WIN:
                    winner = self.x_symbol
                    break

        # check diagonal line
        if winner == None:
            sum = 0

            for h in range(self.height):
                sum += self.board[h, h]

                if sum == self.o_id * NUM_SYMBOL_TO_WIN:
                    winner = self.o_symbol
                    break
                elif sum == self.x_id * NUM_SYMBOL_TO_WIN:
                    winner = self.x_symbol
                    break

        # check diagonal line
        if winner == None:

            sum = 0
            for h in range(self.height):
                sum += self.board[h, self.height - h - 1]

                if sum == self.o_id * NUM_SYMBOL_TO_WIN:
                    winner = self.o_symbol
                    break
                elif sum == self.x_id * NUM_SYMBOL_TO_WIN:
                    winner = self.x_symbol
                    break

        # check draw case
        draw = False

        if winner == None:
            n_empty = 0

            for w in range(self.width):

                for h in range(self.height):
                    if self.board[h, w] != self.empty_id:
                        n_empty += 1

            if n_empty == self.width * self.height:
                # there is no empty cell on the board
                # draw case
                winner = None
                draw = True

        self.winner_symbol = winner

        if draw:
            # there is no available moves on the board. The game will end!
            return True

        else:
            if self.winner_symbol == None:
                # the game is not over
                return False
            else:
                # the game is over
                return True

    def get_winner(self):
        self.is_game_over()
        return self.winner_symbol

    def get_state(self):
        state = '1'  # to avoid '001' -> '1' when converting state to integer

        for h in range(self.height):
            for w in range(self.width):
                state += str(int(self.board[h, w]))  # cast to interger to avoid joining dot delimiter, e.g., 1., 5.

        return int(state)

    def draw_board(self):
        row = ''
        for w in range(self.width):

            row += '-------------\n| '

            for h in range(self.height):
                if self.board[w, h] == self.x_id:
                    row += 'x'
                elif self.board[w, h] == self.o_id:
                    row += 'o'
                else:
                    row += ' '
                row += ' | '
            row += '\n'

        row += '-------------'
        print(row)


if __name__ == '__main__':
    b = Board()
    # b.board[0, 2], b.board[1, 1], b.board[2, 0] = b.O, b.O, b.O
    # b.board[0, 2], b.board[1, 1], b.board[2, 0] = b.X, b.X, b.X
    b.board[0, 0], b.board[0, 1], b.board[1, 2], b.board[2, 0], b.board[2, 1] = b.x_id, b.o_id, b.o_id, b.x_id, b.x_id

    b.draw_board()

    over = b.is_game_over()
    print(f'winner = {b.winner_symbol}')

    print(f'state = {b.get_state()}')
