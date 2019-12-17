from math import inf
import copy
import random
import numpy as np


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
