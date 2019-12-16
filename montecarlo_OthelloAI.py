from OthelloEngine import get_all_moves
import random
import copy
import time
from math import inf

import numpy as np


class Othello_AI:

    def __init__(self, team_type, board_size=8, time_limit=2.0):
        # team_type will be either 'W' or 'B', indicating what color you are
        # board_size and time_limit will likely stay constant, but if you want this can add different challanges
        self.team_type = team_type

    def get_move(self, board_state, turn_number):
        # board state will be an board_size by board_size array with the current state of the game.
        # Possible values are: 'W', 'B', or '-'
        # Return your desired move (If invalid, instant loss)
        # Example move: ('W', (1, 6))
        new_board_state = [turn_number, board_state]
        best_move = monte_carlo_tree_search(copy.deepcopy(new_board_state), self, N=50)
        return best_move


    def actions(self, board_state):
        player = self.to_move(board_state)
        moves = get_all_moves(board_state[1], player)
        if len(moves) == 0:
            return [(player, None)]
        else:
            return moves


    def result(self, board_state, move):
        if move[1] is not None:
            r = move[1][0]
            c = move[1][1]
            color = move[0]

            # left
            i = r
            j = c - 1
            while j >= 0:
                if board_state[1][i][j] != color and board_state[1][i][j] != '-':
                    # it's opposite color, keep checking
                    j -= 1
                else:
                    if board_state[1][i][j] == color:
                        # it's the same color, go back and change till we are at c-1
                        for index in range(c - j - 1):
                            board_state[1][i][j + index + 1] = color
                    # end the loop
                    break

            # left-up direction
            i = r - 1
            j = c - 1
            while i >= 0 and j >= 0:
                if board_state[1][i][j] != color and board_state[1][i][j] != '-':
                    # it's opposite color, keep checking
                    i -= 1
                    j -= 1
                else:
                    if board_state[1][i][j] == color:
                        # it's the same color, go back and change till we are at c-1, r-1
                        for index in range(c - j - 1):
                            board_state[1][i + index + 1][j + index + 1] = color
                    # end the loop
                    break

            # up
            i = r - 1
            j = c
            while i >= 0:
                if board_state[1][i][j] != color and board_state[1][i][j] != '-':
                    # it's opposite color, keep checking
                    i -= 1
                else:
                    if board_state[1][i][j] == color:
                        # it's the same color, go back and change till we are at r-1
                        for index in range(r - i - 1):
                            board_state[1][i + index + 1][j] = color
                    # end the loop
                    break

            # right-up direction
            i = r - 1
            j = c + 1
            while i >= 0 and j < len(board_state[1]):
                if board_state[1][i][j] != color and board_state[1][i][j] != '-':
                    # it's opposite color, keep checking
                    i -= 1
                    j += 1
                else:
                    if board_state[1][i][j] == color:
                        # it's the same color, go back and change till we are at r-1, c+1
                        for index in range(r - i - 1):
                            board_state[1][i + index + 1][j - index - 1] = color
                    # end loop
                    break

            # right direction
            i = r
            j = c + 1
            while j < len(board_state[1]):
                if board_state[1][i][j] != color and board_state[1][i][j] != '-':
                    # it's opposite color, keep checking
                    j += 1
                else:
                    if board_state[1][i][j] == color:
                        # it's the same color, go back and change till we are at c+1
                        for index in range(j - c - 1):
                            board_state[1][i][j - index - 1] = color
                    # end loop
                    break

            # right-down
            i = r + 1
            j = c + 1
            while i < len(board_state[1]) and j < len(board_state[1]):
                if board_state[1][i][j] != color and board_state[1][i][j] != '-':
                    # it's opposite color, keep checking
                    i += 1
                    j += 1
                else:
                    if board_state[1][i][j] == color:
                        # it's the same color, go back and change till we are at r+1,c+1
                        for index in range(j - c - 1):
                            board_state[1][i - index - 1][j - index - 1] = color
                    # end loop
                    break

            # down
            i = r + 1
            j = c
            while i < len(board_state[1]):
                if board_state[1][i][j] != color and board_state[1][i][j] != '-':
                    # it's opposite color, keep checking
                    i += 1
                else:
                    if board_state[1][i][j] == color:
                        # it's the same color, go back and change till we are at r+1
                        for index in range(i - r - 1):
                            board_state[1][i - index - 1][j] = color
                    # end loop
                    break

            # left-down
            i = r + 1
            j = c - 1
            while i < len(board_state[1]) and j >= 0:
                if board_state[1][i][j] != color and board_state[1][i][j] != '-':
                    # it's opposite color, keep checking
                    i += 1
                    j -= 1
                else:
                    if board_state[1][i][j] == color:
                        # it's the same color, go back and change till we are at r+1
                        for index in range(i - r - 1):
                            board_state[1][i - index - 1][j + index + 1] = color
                    # end loop
                    break

            # set the spot in the board_state
            board_state[1][r][c] = color
        board_state[0] += 1
        return board_state


    def terminal_test(self, board_state):
        if len(get_all_moves(board_state[1], 'W')) != 0 or len(get_all_moves(board_state[1], 'B')) != 0:
            return False
        else:
            return True


    def to_move(self, board_state):
        if board_state[0] % 2 == 1:
            return 'W'
        else:
            return 'B'


    def utility(self, board_state, player):
        # The idea behind this utility is that your total pieces compared to the opponents total pieces
        # determines who wins and by how much at the end of a game. Subtracting your opponents pieces from yours
        # will determine how much your opponent owes you (if you win), or how much you owe your opponent (if they win).

        white_count = sum(row.count('W') for row in board_state[1])
        black_count = sum(row.count('B') for row in board_state[1])

        if player == 'W':
            teamCount = white_count
            opponentCount = black_count
        else:
            teamCount = black_count
            opponentCount = white_count
        return teamCount - opponentCount


    def get_team_name(self):
        # returns a string containing your team name
        return "Monte Carlo Bot"


# Monte Carlo tree node and ucb function
class MCT_Node:
    """Node in the Monte Carlo search tree, keeps track of the children states."""

    def __init__(self, parent=None, state=None, U=0, N=0):
        self.__dict__.update(parent=parent, state=state, U=U, N=N)
        self.children = {}
        self.actions = None


def ucb(n, C=1.4):
    return np.inf if n.N == 0 else n.U / n.N + C * np.sqrt(np.log(n.parent.N) / n.N)

# Monte Carlo search
def monte_carlo_tree_search(state, game, N=1000):
    def select(n):
        """select a leaf node in the tree"""
        if n.children:
            return select(max(n.children.keys(), key=ucb))
        else:
            return n

    def expand(n):
        """expand the leaf node by adding all its children states"""
        if not n.children and not game.terminal_test(n.state):
            n.children = {MCT_Node(state=game.result(copy.deepcopy(n.state), action), parent=n): action
                          for action in game.actions(n.state)}
        return select(n)

    def simulate(game, state):
        """simulate the utility of current state by random picking a step"""
        player = game.to_move(state)
        while not game.terminal_test(state):
            action = random.choice(list(game.actions(state)))
            state = game.result(copy.deepcopy(state), action)
        v = game.utility(state, player)
        return -v

    def backprop(n, utility):
        """passing the utility back to all parent nodes"""
        if utility > 0:
            n.U += utility
        # if utility == 0:
        #     n.U += 0.5
        n.N += 1
        if n.parent:
            backprop(n.parent, -utility)

    root = MCT_Node(state=state)

    for _ in range(N):
        leaf = select(root)
        child = expand(leaf)
        result = simulate(game, child.state)
        backprop(child, result)

    max_state = max(root.children, key=lambda p: p.N)

    return root.children.get(max_state)


#___________UNIT TESTING___________
if __name__ == "__main__":
    testBot = Othello_AI('B')
    board_state = [['-' for i in range(8)] for j in range(8)]
    board_state[8 // 2 - 1][8 // 2 - 1] = "W"
    board_state[8 // 2][8 // 2] = "W"
    board_state[8 // 2 - 1][8 // 2] = "B"
    board_state[8 // 2][8 // 2 - 1] = "B"
    print(testBot.get_move(board_state))
