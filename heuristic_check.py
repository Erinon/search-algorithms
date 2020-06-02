"""Performing heuristic checks.
    
A module that provides functions that perform heuristic checks. Checks include
optimistic and consistent properties.
    
"""

from util import flip_transitions
from search import dijkstra


def is_optimistic(h, trans, goal):
    """Checks if heuristic is optimistic.

    Function that performs optimistic check on given heuristic function.
    Heuristic is optimistic if it never overestimates the real cost from the
    current state to the end state. Real costs are calculated using dijkstra
    algorithm. Also prints out the check and errors if optimistic property is
    violated.

    Args:
        h: Heuristic function that is being checked.
        trans: A dictionary containing list of possible transitions and their
            costs for each key that represents the state name.
        goal: List of goal states represented by string name of the state.

    Returns:
        Boolean indicating whether the heuristic is optimistic or not.
    
    """
    print('Checking if heuristic is optimistic.')
    
    costs = dijkstra(goal, flip_transitions(trans))
    
    errors = []
    
    for s in trans:
        hs = h(s)
        if hs > costs[s]:
            errors.append((s, hs, costs[s]))
    
    print_optimistic_check(errors)
    
    return not errors


def print_optimistic_check(errors):
    """Prints optimistic check results.

    Function that prints the results of optimistic check. If heuristic is not
    optimistic, also prints out the errors.

    Args:
        errors: List of errors where optimistic property is violated.
    
    """
    error_num = len(errors)
    
    if error_num == 0:
        print('Heuristic is optimistic.')
    else:        
        if error_num > 10:
            print('  [ERR] {} errors, omitting output.'.format(error_num))
        else:
            for s, h, hs in errors:
                print('  [ERR] h({}) > h*: {} > {}'.format(s, h, hs))
        
        print('Heuristic is not optimistic.')


def is_consistent(h, trans):
    """Checks if heuristic is consistent.

    Function that performs consistency check on given heuristic function.
    Heuristic is consistent if it changes by cost at most. Also prints out the
    check and errors if consistency property is violated.
    violated.

    Args:
        h: Heuristic function that is being checked.
        trans: A dictionary containing list of possible transitions and their
            costs for each key that represents the state name.

    Returns:
        Boolean indicating whether the heuristic is consistent or not.
    
    """
    print('Checking if heuristic is consistent.')
    
    errors = []
    
    for s1 in trans:
        for s2, cost in trans[s1]:
            h1, h2 = h(s1), h(s2)
            if h1 > h2 + cost:
                errors.append((s1, s2, h1, h2, cost))
    
    print_consistent_check(errors)
    
    return not errors


def print_consistent_check(errors):
    """Prints consistency check results.

    Function that prints the results of consistency check. If heuristic is not
    consistent, also prints out the errors.

    Args:
        errors: List of errors where consistency property is violated.
    
    """
    error_num = len(errors)
    
    if error_num == 0:
        print('Heuristic is consistent.')
    else:        
        if error_num > 10:
            print('  [ERR] {} errors, omitting output.'.format(error_num))
        else:
            for s1, s2, h1, h2, c in errors:
                print('  [ERR] h({}) > h({}) + c: {} > {} + {}'.format(s1, s2, h1, h2, c))
        
        print('Heuristic is not consistent.')

