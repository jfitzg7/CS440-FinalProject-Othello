from OthelloEngine import get_all_moves
import random
import copy
from math import inf
from algorithms import alpha_beta_cutoff_search


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
        best_move = alpha_beta_cutoff_search(copy.deepcopy(board_state), self, d=4, eval_fn=self.subtractOpponentsPiecesUtility)
        return best_move


    def actions(self, board_state, player):
        moves = get_all_moves(board_state, player)
        if len(moves) == 0:
            return [(self.team_type, None)]
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
                if board_state[i][j] != color and board_state[i][j] != '-':
                    # it's opposite color, keep checking
                    j -= 1
                else:
                    if board_state[i][j] == color:
                        # it's the same color, go back and change till we are at c-1
                        for index in range(c - j - 1):
                            board_state[i][j + index + 1] = color
                    # end the loop
                    break

            # left-up direction
            i = r - 1
            j = c - 1
            while i >= 0 and j >= 0:
                if board_state[i][j] != color and board_state[i][j] != '-':
                    # it's opposite color, keep checking
                    i -= 1
                    j -= 1
                else:
                    if board_state[i][j] == color:
                        # it's the same color, go back and change till we are at c-1, r-1
                        for index in range(c - j - 1):
                            board_state[i + index + 1][j + index + 1] = color
                    # end the loop
                    break

            # up
            i = r - 1
            j = c
            while i >= 0:
                if board_state[i][j] != color and board_state[i][j] != '-':
                    # it's opposite color, keep checking
                    i -= 1
                else:
                    if board_state[i][j] == color:
                        # it's the same color, go back and change till we are at r-1
                        for index in range(r - i - 1):
                            board_state[i + index + 1][j] = color
                    # end the loop
                    break

            # right-up direction
            i = r - 1
            j = c + 1
            while i >= 0 and j < len(board_state):
                if board_state[i][j] != color and board_state[i][j] != '-':
                    # it's opposite color, keep checking
                    i -= 1
                    j += 1
                else:
                    if board_state[i][j] == color:
                        # it's the same color, go back and change till we are at r-1, c+1
                        for index in range(r - i - 1):
                            board_state[i + index + 1][j - index - 1] = color
                    # end loop
                    break

            # right direction
            i = r
            j = c + 1
            while j < len(board_state):
                if board_state[i][j] != color and board_state[i][j] != '-':
                    # it's opposite color, keep checking
                    j += 1
                else:
                    if board_state[i][j] == color:
                        # it's the same color, go back and change till we are at c+1
                        for index in range(j - c - 1):
                            board_state[i][j - index - 1] = color
                    # end loop
                    break

            # right-down
            i = r + 1
            j = c + 1
            while i < len(board_state) and j < len(board_state):
                if board_state[i][j] != color and board_state[i][j] != '-':
                    # it's opposite color, keep checking
                    i += 1
                    j += 1
                else:
                    if board_state[i][j] == color:
                        # it's the same color, go back and change till we are at r+1,c+1
                        for index in range(j - c - 1):
                            board_state[i - index - 1][j - index - 1] = color
                    # end loop
                    break

            # down
            i = r + 1
            j = c
            while i < len(board_state):
                if board_state[i][j] != color and board_state[i][j] != '-':
                    # it's opposite color, keep checking
                    i += 1
                else:
                    if board_state[i][j] == color:
                        # it's the same color, go back and change till we are at r+1
                        for index in range(i - r - 1):
                            board_state[i - index - 1][j] = color
                    # end loop
                    break

            # left-down
            i = r + 1
            j = c - 1
            while i < len(board_state) and j >= 0:
                if board_state[i][j] != color and board_state[i][j] != '-':
                    # it's opposite color, keep checking
                    i += 1
                    j -= 1
                else:
                    if board_state[i][j] == color:
                        # it's the same color, go back and change till we are at r+1
                        for index in range(i - r - 1):
                            board_state[i - index - 1][j + index + 1] = color
                    # end loop
                    break

            # set the spot in the board_state
            board_state[r][c] = color

        return board_state


    def terminal_test(self, board_state):
        if len(get_all_moves(board_state, 'W')) != 0 or len(get_all_moves(board_state, 'B')) != 0:
            return False
        else:
            return True


    def to_move(self):
        return self.team_type


    def totalPieceUtility(self, board_state, player):
        #__________total team piece count utility__________
        totalPieceCount = 0
        if player == 'W':
            white_count = sum(row.count('W') for row in board_state)
            totalPieceCount = white_count
        else:
            black_count = sum(row.count('B') for row in board_state)
            totalPieceCount = black_count
        return totalPieceCount

    def subtractOpponentsPiecesUtility(self, board_state, player):
        # The idea behind this utility is that your total pieces compared to the opponents total pieces
        # determines who wins and by how much at the end of a game. Subtracting your opponents pieces from yours
        # will determine how much your opponent owes you (if you win), or how much you owe your opponent (if they win).

        white_count = sum(row.count('W') for row in board_state)
        black_count = sum(row.count('B') for row in board_state)

        if player == 'W':
            teamCount = white_count
            opponentCount = black_count
        else:
            teamCount = black_count
            opponentCount = white_count
        return teamCount - opponentCount


    def get_team_name(self):
        # returns a string containing your team name
        return "Alpha-beta bot"


#___________UNIT TESTING___________
if __name__ == "__main__":
    testBot = Othello_AI('B')
    board_state = [['-' for i in range(8)] for j in range(8)]
    board_state[8 // 2 - 1][8 // 2 - 1] = "W"
    board_state[8 // 2][8 // 2] = "W"
    board_state[8 // 2 - 1][8 // 2] = "B"
    board_state[8 // 2][8 // 2 - 1] = "B"
    testBot.get_move(board_state)
