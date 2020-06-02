"""Implementation of various path-finding algorithms.
    
A module that provides functions that perform various path-finding
algorithms. Algorithms also print the search results.

"""

from util import Stack, Queue, PriorityQueue


class Node():
    """Node in state space graph.

    A class that is used for representing a single node/state in the state
    space graph.

    Attributes:
        s: A string representing the state name.
        d: An integer representing the depth of the node in state space
            graph.
        p: Node representing the parent node or None if this is the start
            node.
        c: A float representing the cost of moving to this node.
        h: A float representing the node's heuristic value.
    """
    
    def __init__(self, s, d=0, p=None, c=0., h=0.):
        """Inits Node with given parameters."""
        self.s = s
        self.d = d
        self.p = p
        self.c = c
        self.h = h
    
    def path(self):
        """Returns path to this node using backtracking."""
        path = [self.s]
        
        parent = self.p
        while parent:
            path[:0] = [parent.s]
            parent = parent.p
        
        return path
    
    def __lt__(self, other):
        """Overrides < operator using cost and heuristic values"""
        return self.c + self.h < other.c + other.h


def BFS(s0, trans, goal):
    """Performs a breadth-first search.

    Performs a breadth-first search starting from state s0 and trying to reach
    goal state, if it exists. Search also prints out the results if the path is
    found.

    Args:
        s0: String representing the name of the starting state.
        trans: A dictionary containing list of possible transitions and their
            costs for each key that represents the state name.
        goal: A list of goal state names.

    Returns:
        A list representing the path from s0 to one of the goal states if the
        path is found, else returns None
    
    """
    print('Running bfs:')
    
    open = Queue()
    open.push(Node(s0))
    
    visited = set()
    
    while open:
        n = open.pop()
        
        visited.add(n.s)
        
        if n.s in goal:
            path = n.path()
            print_search_results(path, len(visited))
            return path
        
        for m, _ in trans.get(n.s, []):
            if m not in visited:
                open.push(Node(m, n.d + 1, n))
    
    print('Path not found.')
    
    return None


def UCS(s0, trans, goal):
    """Performs a uniform-cost search.

    Performs a uniform-cost search starting from state s0 and trying to reach
    goal state, if it exists. Search also prints out the results if the path is
    found.

    Args:
        s0: String representing the name of the starting state.
        trans: A dictionary containing list of possible transitions and their
            costs for each key that represents the state name.
        goal: A list of goal state names.

    Returns:
        A list representing the path from s0 to one of the goal states if the
        path is found, else returns None
    
    """
    print('Running ucs:')
    
    open = PriorityQueue()
    open.push(Node(s0))
    
    visited = set()
    
    while open:
        n = open.pop()
        
        visited.add(n.s)
        
        if n.s in goal:
            path = n.path()
            print_search_results(path, len(visited), n.c)
            return path
        
        for m, c in trans.get(n.s, []):
            if m not in visited:
                open.push(Node(m, n.d + 1, n, n.c + c))
    
    print('Path not found.')
    
    return None


def DFS(s0, trans, goal):
    """Performs a depth-first search.

    Performs a depth-first search starting from state s0 and trying to reach
    goal state, if it exists. Search also prints out the results if the path is
    found.

    Args:
        s0: String representing the name of the starting state.
        trans: A dictionary containing list of possible transitions and their
            costs for each key that represents the state name.
        goal: A list of goal state names.

    Returns:
        A list representing the path from s0 to one of the goal states if the
        path is found, else returns None
    
    """
    print('Running dfs:')
    
    open = Stack()
    open.push(Node(s0))
    
    visited = set()
    
    while open:
        n = open.pop()
        
        visited.add(n.s)
        
        if n.s in goal:
            path = n.path()
            print_search_results(path, len(visited))
            return path
        
        for m, _ in trans.get(n.s, []):
            if m not in visited:
                open.push(Node(m, n.d + 1, n))
    
    print('Path not found.')
    
    return None


def lDFS(s0, trans, goal, k, show=True, visited_before=0):
    """Performs a limited depth-first search.

    Performs a limited depth-first search starting from state s0 and trying to
    reach goal state, if it exists. Search also prints out the results if the
    path is found.

    Args:
        s0: String representing the name of the starting state.
        trans: A dictionary containing list of possible transitions and their
            costs for each key that represents the state name.
        goal: A list of goal state names.
        k: An integer representing the depth limmit of the search.
        show: A boolean indicating whether the function should print results.

    Returns:
        A list representing the path from s0 to one of the goal states if the
        path is found, else returns None. If variable show is False, returns
        the number of visited states instead, because then it is used by IDF
        search algorithm.
    
    """
    if show:
        print('Running limited dfs:')
    
    open = Stack()
    open.push(Node(s0))
    
    visited = {}
    
    while open:
        n = open.pop()
        
        visited[n.s] = n.d
        
        if n.s in goal:
            path = n.path()
            print_search_results(path, visited_before + len(visited))
            return path
        
        if n.d < k:
            for m, _ in trans.get(n.s, []):
                if m not in visited or n.d + 1 < visited[m]:
                    open.push(Node(m, n.d + 1, n))
    
    if not show:
        return len(visited)
    
    print('Path not found.')
    
    return None


def IDS(s0, trans, goal):
    """Performs a iterative deepening search.

    Performs a iterative deepening search starting from state s0 and trying to
    reach goal state, if it exists. Search also prints out the results if the
    path is found.

    Args:
        s0: String representing the name of the starting state.
        trans: A dictionary containing list of possible transitions and their
            costs for each key that represents the state name.
        goal: A list of goal state names.

    Returns:
        A list representing the path from s0 to one of the goal states if the
        path is found, else returns None
    
    """
    print('Running ids:')
    
    visited = 0
    for k in range(100):
        res = lDFS(s0, trans, goal, k, False, visited)
        
        if type(res) is list:
            return res
        
        visited += res
        
        k += 1
    
    print('Path not found.')
    
    return None


def GBFS(s0, trans, goal, h):
    """Performs a greedy best-first search.

    Performs a greedy best-first search starting from state s0 and trying to
    reach goal state, if it exists. Search also prints out the results if the
    path is found.

    Args:
        s0: String representing the name of the starting state.
        trans: A dictionary containing list of possible transitions and their
            costs for each key that represents the state name.
        goal: A list of goal state names.

    Returns:
        A list representing the path from s0 to one of the goal states if the
        path is found, else returns None
    
    """
    print('Running gbfs:')

    open = PriorityQueue()
    open.push(Node(s0))
    
    visited = set()
    
    while open:
        n = open.pop()
        
        visited.add(n.s)
        
        if n.s in goal:
            path = n.path()
            print_search_results(path, len(visited))
            return path
        
        for m, c in trans.get(n.s, []):
            if m not in visited:
                open.push(Node(m, n.d + 1, n, h=h(m)))
    
    print('Path not found.')
    
    return None


def HCS(s0, trans, h):
    """Performs a hill climb search.

    Performs a hill climb search starting from state s0 and trying to reach
    goal state, if it exists. Search also prints out the results if the path is
    found.

    Args:
        s0: String representing the name of the starting state.
        trans: A dictionary containing list of possible transitions and their
            costs for each key that represents the state name.
        goal: A list of goal state names.

    Returns:
        A list representing the path from s0 to one of the goal states if the
        path is found, else returns None
    
    """
    print('Running hcs:')
    
    n = Node(s0)
    
    while True:
        M = trans.get(n.s, [])
        
        if not M:
            break
        
        m = None
        hm = float('inf')
        
        for s, _ in M:
            hs = h(s)
            
            if hs < hm:
                m = s
                hm = hs
        
        if n.h < hm:
            break
        
        n = Node(m, n.d + 1, n, h=hm)
    
    path = n.path()
    print_search_results(path, n.d + 1)
    return path


def AStar(s0, trans, goal, h):
    """Performs an A* search.

    Performs an A* search starting from state s0 and trying to reach
    goal state, if it exists. Search also prints out the results if the path is
    found.

    Args:
        s0: String representing the name of the starting state.
        trans: A dictionary containing list of possible transitions and their
            costs for each key that represents the state name.
        goal: A list of goal state names.

    Returns:
        A list representing the path from s0 to one of the goal states if the
        path is found, else returns None
    
    """
    print('Running astar:')
    
    open = PriorityQueue()
    open.push(Node(s0))
    
    closed = {}
    
    while open:
        n = open.pop()
        
        closed[n.s] = n.c
        
        if n.s in goal:
            path = n.path()
            print_search_results(path, len(closed), n.c)
            return path
        
        for m, c in trans.get(n.s, []):
            if m not in closed or closed[m] > n.c + c:
                open.push(Node(m, n.d + 1, n, n.c + c, h(m)))
    
    print('Path not found.')
    
    return None


def print_search_results(path, visited, cost=None):
    """Prints search results.

    A function that prints out search results nicely.

    Args:
        path: A list of state names representing the found path.
        visited: A list of states representing all visited states during the
            search.
        cost: A float representing the total cost of a path, or None if
            search does not use cost information.
    
    """
    print('States visited = {}'.format(visited))
    
    if cost:
        print('Found path of length {} with total cost {}:'.format(len(path), cost))
    else:
        print('Found path of length {}:'.format(len(path)))
    
    print(' =>\n'.join(path))


def dijkstra(start_states, trans):
    """Performs a dijsktra search.

    Performs a dijkstra search starting from states in start_states and trying
    to reach every other state.

    Args:
        start_states: A list of starting states' names.
        trans: A dictionary containing list of possible transitions and their
            costs for each key that represents the state name.

    Returns:
        A dictionary representing the cost to get to each state from the
        closest starting state.
    
    """
    costs = {}
    
    open = PriorityQueue()
    
    visited = set()
    
    for s0 in start_states:
        costs[s0] = 0.
        open.push((0., s0))
    
    while open:
        d, n = open.pop()
        
        if n in visited:
            continue
        
        visited.add(n)
        
        if n not in costs:
            costs[n] = float('inf')
        
        for m, c in trans.get(n, []):
            if m not in costs:
                costs[m] = float('inf')
            
            if costs[n] + c < costs[m]:
                costs[m] = costs[n] + c
                open.push((costs[m], m))
    
    return costs

