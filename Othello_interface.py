from OthelloEngine import get_all_moves
import random


class Othello_AI:

    def __init__(self, team_type, board_size=8, time_limit=2.0):
        # team_type will be either 'W' or 'B', indicating what color you are
        # board_size and time_limit will likely stay constant, but if you want this can add different challanges
        self.team_type = team_type

    def get_move(self, board_state):
        # board state will be an board_size by board_size array with the current state of the game.
        # Possible values are: 'W', 'B', or '-'
        # Return your desired move (If invalid, instant loss)
        # Example move: ('W', (1, 6))
        moves = get_all_moves(board_state, self.team_type)
        if len(moves) > 0:
            return random.choice(moves)
        return None

    def actions(self, board_state):
        return get_all_moves(board_state, self.team_type)

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

        pass

    def terminal_test(self, board_state):
        if len(get_all_moves(board_state, 'W')) != 0 or len(get_all_moves(board_state, 'B')) != 0:
            return False
        else:
            return True


def get_team_name(self):
    # returns a string containing your team name
    return "Default bot"
