"""Support for loading state spaces and heuristics from files.
    
A module that provides functions that handle loading of state space and
heuristic functions from files in specific configuration.
    
"""


def get_state_space(fname):
    """Loads state space from a file.

    Function that loads state space from a file.
    

    Args:
        fname: String representing path to a file containing state space.

    Returns:
        A tuple (s0, transitions, goal).
        s0: Starting state name as string.
        transitions: A dictionary containing list of possible transitions and
            their costs for each key that represents the state name.
        goal: A list of goal state names.
    
    """
    s0 = None
    transitions = dict()
    goal = set()
    
    total_transitions = 0
    
    with open(fname) as f:
        for l in f:
            l = l.strip()
            
            if l[0] == '#':
                continue
            
            if not s0:
                s0 = l
                continue
            
            l_spl = l.split()
            
            if not goal:
                for g in l_spl:
                    goal.add(g)
                
                continue
            
            s = l_spl[0][:-1]
            
            if s not in transitions:
                transitions[s] = set()
            
            for i in range(1, len(l_spl)):
                t = l_spl[i].split(',')
                transitions[s].add((t[0].strip(), float(t[1].strip())))
                
                total_transitions += 1
    
    print_state_space(s0, goal, len(transitions), total_transitions)
    
    return s0, transitions, goal


def print_state_space(s0, goal, states, transitions):
    """Prints information about state space.

    Function that nicely prints some information about given state space.
    

    Args:
        s0: Starting state name as string.
        goal: A list of goal state names.
        states: A list of all states
        transitions: A dictionary containing list of possible transitions and
            their costs for each key that represents the state name.

    Returns:
        A tuple (s0, transitions, goal).
        s0: Starting state name as string
        transitions: A dictionary containing list of possible transitions and
        their costs for each key that represents the state name.
        goal: A list of goal state names.
    
    """
    print('Start state: {}'.format(s0))
    print('End state(s): [{}]'.format(', '.join([f'\'{g}\'' for g in goal])))
    print('State space size: {}'.format(states))
    print('Total transitions: {}'.format(transitions))


def get_heuristic(fname):
    """Loads heuristic function from a file.

    Function that loads heuristic function from a file.
    

    Args:
        fname: String representing path to a file containing heuristic
        function.

    Returns:
        A function that takes state name and returns heuristic value of that
        state as provided in the heuristic file.
    
    """
    heuristic = dict()
    
    with open(fname) as f:
        for l in f:
            l = l.strip()
            
            if l[0] == '#':
                continue
            
            l_spl = l.split()
            
            heuristic[l_spl[0][:-1]] = float(l_spl[1])
    
    return lambda s: heuristic[s]

