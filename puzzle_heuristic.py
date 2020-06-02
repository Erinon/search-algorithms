"""8-puzzle heuristic functions.
    
Module that provides heuristic functions for 8-puzzle that are based on
specific states and calculated, not loaded from files.
Currently, only one heuristic is implemented.
    
"""


def manhattan_distance(goals):
    """Manhattan distance heuristic

    Function that returns a function that gives manhattan distance heuristic
    value for each given state.

    Args:
        goals: List of goal states represented by string name of the state.

    Returns:
        Returns a function that gives manhattan distance heuristic
        value for each given state.
    
    """
    new_goals = []
    
    for g in goals:
        new_goals.append({})
        
        row = 0
        for c in range(len(g)):
            if g[c] != '_':
                new_goals[-1][g[c]] = c - row
            else:
                row += 1
    
    def heuristic(state):
        h = float('inf')
        
        for g in new_goals:
            current_h = 0
            
            row = 0
            for c in range(len(state)):
                if state[c] != '_':
                    current_h += abs((c - row) % 3 - g[state[c]] % 3) + abs((c - row) // 3 - g[state[c]] // 3)
                else:
                    row += 1
            
            if current_h < h:
                h = current_h
        
        return h
    
    return heuristic

