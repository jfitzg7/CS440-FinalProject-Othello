from math import inf
import copy


#Depth-limited minimax algorithm, modified version from aimapython
def minimax_cutoff(state, game, d=4, cutoff_test=None, eval_fn=None):
    minPlayer = ''
    maxPlayer = game.to_move()
    if maxPlayer == 'W':
        minPlayer = 'B'
    else:
        minPlayer = 'W'

    def max_value(state, depth):
        if cutoff_test(state, depth):
            return eval_fn(state, maxPlayer)
        v = -inf
        for a in game.actions(state, maxPlayer):
            v = max(v, min_value(game.result(state, a), depth + 1))
        return v

    def min_value(state, depth):
        if cutoff_test(state, depth):
            return eval_fn(state, maxPlayer)
        v = inf
        for a in game.actions(state, minPlayer):
            v = min(v, max_value(game.result(state, a), depth + 1))
        return v

    # Body of minmax_decision:
    cutoff_test = (cutoff_test or (lambda state, depth: depth > d or game.terminal_test(state)))
    eval_fn = eval_fn or (lambda state, player: game.utility(state, player))
    return max(game.actions(state, maxPlayer), key=lambda a: min_value(game.result(state, a), 1))


#Alpha-beta cutoff from aimapython repository
def alpha_beta_cutoff_search(state, game, d=4, cutoff_test=None, eval_fn=None):
    minPlayer = ''
    maxPlayer = game.to_move()
    if maxPlayer == 'W':
        minPlayer = 'B'
    else:
        minPlayer = 'W'

    # Functions used by alpha_beta
    def max_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(state, maxPlayer)
        v = -inf
        for a in game.actions(state, maxPlayer):
            v = max(v, min_value(game.result(copy.deepcopy(state), a), alpha, beta, depth + 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(state, maxPlayer)
        v = inf
        for a in game.actions(state, minPlayer):
            v = min(v, max_value(game.result(copy.deepcopy(state), a), alpha, beta, depth + 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Body of alpha_beta_cutoff_search starts here:
    # The default test cuts off at depth d or at a terminal state
    cutoff_test = (cutoff_test or (lambda state, depth: depth > d or game.terminal_test(state)))
    eval_fn = eval_fn or (lambda state, player: game.utility(state, player))
    best_score = -inf
    beta = inf
    best_action = None
    for a in game.actions(state, maxPlayer):
        v = min_value(game.result(copy.deepcopy(state), a), best_score, beta, 1)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action
