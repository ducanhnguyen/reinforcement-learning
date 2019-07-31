import numpy as np


class Board:
    '''
    Represent a grid board (4x4 by default)
    '''

    def __init__(self, width=4, height=4):
        self.width = width
        self.height = height

        self.ACTIONS = dict()
        self.ACTIONS['UP'] = 0  # can not be changed
        self.ACTIONS['DOWN'] = 1  # can not be changed
        self.ACTIONS['LEFT'] = 2  # can not be changed
        self.ACTIONS['RIGHT'] = 3  # can not be changed
        self.ACTIONS['NO_ACTION'] = -1  # can not be changed

        # actions: up, down, left, right
        self.NUM_OF_ACTIONS = 4  # can not be changed

        # create value function
        self.V = np.zeros(shape=(self.height, self.width))

        # ------------------------------------------
        # BEGIN OF MODIFICATION
        # you can modify obstacles, rewards, terminal states, and the starting state
        self.define_obstacles()
        self.define_rewards()
        self.define_terminal_states()
        self.define_starting_state()
        # END OF MODIFICATION
        # ------------------------------------------

        self.define_possible_actions()
        self.initialize_actions()

    def define_starting_state(self):
        '''
        define the starting state
        :return:
        '''
        self.start_state = [3, 0]
        self.current_state = [self.start_state[0], self.start_state[1]]

    def define_terminal_states(self):
        '''
        create terminal states
        :return:
        '''
        self.terminal_states = np.zeros(shape=(self.height, self.width))
        self.terminal_states[0, 3] = True
        self.terminal_states[1, 3] = True

    def define_obstacles(self):
        '''
        create obstacles
        :return:
        '''
        self.obstables = np.zeros(shape=(self.height, self.width))
        self.obstables[2, 1] = True

    def define_rewards(self):
        '''
        create rewards
        :return:
        '''
        self.rewards = np.zeros(shape=(self.height, self.width))
        self.rewards[0, 3] = 1
        self.rewards[1, 3] = -1

    def initialize_actions(self):
        '''
        Define the valid action for each state.
        Each state just has one action.
        We will change the actions of state using policy iteration.
        :return:
        '''
        self.current_actions = np.zeros(shape=(self.height, self.width))
        for i in range(self.height):
            for j in range(self.width):
                self.current_actions[i, j] = self.ACTIONS['NO_ACTION']

    def define_possible_actions(self):
        '''
        Define the valid actions for each state
        :return:
        '''
        self.possible_actions = np.zeros(shape=(self.height, self.width, self.NUM_OF_ACTIONS))

        # All states have no action associated with it
        for i in range(self.height):
            for j in range(self.width):
                for k in range(self.NUM_OF_ACTIONS):
                    self.possible_actions[i, j, k] = self.ACTIONS['NO_ACTION']

        # Find all possible actions of a state
        for i in range(self.height):
            for j in range(self.width):

                if not self.obstables[i, j] and not self.terminal_states[i, j]:
                    if i - 1 >= 0 and not self.obstables[i - 1, j]:
                        self.possible_actions[i, j, self.ACTIONS['UP']] = True

                    if i + 1 < self.height and not self.obstables[i + 1, j]:
                        self.possible_actions[i, j, self.ACTIONS['DOWN']] = True

                    if j - 1 >= 0 and not self.obstables[i, j - 1]:
                        self.possible_actions[i, j, self.ACTIONS['LEFT']] = True

                    if j + 1 < self.width and not self.obstables[i, j + 1]:
                        self.possible_actions[i, j, self.ACTIONS['RIGHT']] = True

    def get_possible_actions_of_a_state(self, i, j):
        '''
        Get all possible actions of a state
        :param i: the row index of the state
        :param j: the column index of the state
        :return: all possible actions of a state
        '''
        actions = []
        if self.possible_actions[i, j, self.ACTIONS['UP']] == True:
            actions.append(self.ACTIONS['UP'])

        if self.possible_actions[i, j, self.ACTIONS['DOWN']] == True:
            actions.append(self.ACTIONS['DOWN'])

        if self.possible_actions[i, j, self.ACTIONS['LEFT']] == True:
            actions.append(self.ACTIONS['LEFT'])

        if self.possible_actions[i, j, self.ACTIONS['RIGHT']] == True:
            actions.append(self.ACTIONS['RIGHT'])

        return actions

    def get_all_states(self):
        '''
        Get all states on the board (ignore obstacles on the board)
        :return:
        '''
        self.states = []

        for i in range(self.height):
            for j in range(self.width):
                if not self.obstables[i, j]:
                    self.states.append([i, j])

        return self.states

    def move(self, action):
        '''
        Take an action on the board from the current state
        :param action:
        :return:
        '''
        if action == self.ACTIONS['UP']:
            self.current_state[0] -= 1

        elif action == self.ACTIONS['DOWN']:
            self.current_state[0] += 1

        elif action == self.ACTIONS['LEFT']:
            self.current_state[1] -= 1

        elif action == self.ACTIONS['RIGHT']:
            self.current_state[1] += 1

        assert self.current_state[0] >= 0 and self.current_state[0] < self.height and self.current_state[1] >= 0 and \
               self.current_state[1] < self.width

    def unmove(self, action):
        '''
        Undo the action
        :param action:
        :return:
        '''
        if action == self.ACTIONS['UP']:
            self.current_state[0] += 1

        elif action == self.ACTIONS['DOWN']:
            self.current_state[0] -= 1

        elif action == self.ACTIONS['LEFT']:
            self.current_state[1] += 1

        elif action == self.ACTIONS['RIGHT']:
            self.current_state[1] -= 1

        assert self.current_state[0] >= 0 and self.current_state[0] < self.height and self.current_state[1] >= 0 and \
               self.current_state[1] < self.width

    def get_current_reward(self):
        '''
        Get the current reward of the board
        :return:
        '''
        return self.rewards[self.current_state[0], self.current_state[1]]

    def print_current_actions(self):
        '''
        (Just for testing)
        Print the current action of states
        :return:
        '''
        for i in range(self.height):
            print('--------------------')

            row = '|'
            for j in range(self.width):
                action_str = ''

                if self.current_actions[i, j] == self.ACTIONS['UP']:
                    action_str = 'U'

                elif self.current_actions[i, j] == self.ACTIONS['DOWN']:
                    action_str = 'D'

                elif self.current_actions[i, j] == self.ACTIONS['LEFT']:
                    action_str = 'L'

                elif self.current_actions[i, j] == self.ACTIONS['RIGHT']:
                    action_str = 'R'

                if len(action_str) == 0:
                    # the current state has no action
                    row += '   | '
                else:
                    row += ' ' + action_str + ' | '

            print(row)
        print('--------------------')

    def print_value_functions(self):
        '''
        (Just for testing)
        Print the value function of the board
        :return:
        '''
        for i in range(self.height):
            print('-------------------------')

            row = '|'
            for j in range(self.width):
                if self.obstables[i, j]:
                    row += '  x  |'
                else:
                    if self.V[i, j] >= 0:
                        row += ' %.2f|' % self.V[i, j]
                    else:
                        row += '%.2f|' % self.V[i, j]
            print(row)
        print('-------------------------')

    def print_possible_actions(self):
        '''
        (Just for testing)
        Print all possible actions of states on the board
        :return:
        '''
        # iterate over all states
        for i in range(self.height):
            for j in range(self.width):
                possible = self.get_possible_actions_of_a_state(i, j)

                str = ''
                for item in possible:
                    if item == self.ACTIONS['UP']:
                        str += 'U '

                    elif item == self.ACTIONS['DOWN']:
                        str += 'D '

                    elif item == self.ACTIONS['RIGHT']:
                        str += 'R '

                    elif item == self.ACTIONS['LEFT']:
                        str += 'L '

                print(f'State ({i}, {j}): {str}')


if __name__ == '__main__':
    board = Board()

    print('Value functions')
    board.print_value_functions()

    print('All actions:')
    board.print_current_actions()

    print('All possible actions:')
    board.print_possible_actions()
