"""Helper classes and functions.
    
A module that provides some helper classes for data structures and
manipulations and also some helper functions.
    
"""

from heapq import heappush, heappop


class Stack():
    """Stack class.

    Implementation of last-in-first-out (LIFO) data structure.

    """
    
    def __init__(self):
        """Initializes the empty structure."""
        self.items = []
    
    def push(self, item):
        """Adds new item to the structure."""
        self.items.append(item)
    
    def pop(self):
        """Removes and returns the last added element to the structure."""
        return self.items.pop()
    
    def __bool__(self):
        """Overrides the bool operation that returns whether the structure is
           not empty.
        """
        return bool(self.items)


class Queue():
    """Queue class.

    Implementation of first-in-first-out (FIFO) data structure.

    """
    
    def __init__(self):
        """Initializes the empty structure."""
        self.items = []
    
    def push(self, item):
        """Adds new item to the structure."""
        self.items.append(item)
    
    def pop(self):
        """Removes and returns the first added element to the structure."""
        return self.items.pop(0)
    
    def __bool__(self):
        """Overrides the bool operation that returns whether the structure is
           not empty.
        """
        return bool(self.items)


class PriorityQueue():
    """PriorityQueue class.

    Implementation of priority data structure. It always returns the value
    with the lowest value.

    """
    
    def __init__(self):
        """Initializes the empty structure."""
        self.items = []
    
    def push(self, item):
        """Adds new item to the structure."""
        heappush(self.items, item)
    
    def pop(self):
        """Removes and returns the element with the lowest value from the
            structure.
        """
        return heappop(self.items)
    
    def __bool__(self):
        """Overrides the bool operation that returns whether the structure is
           not empty.
        """
        return bool(self.items)


def flip_transitions(trans):
    """Flips transitions in a state space.

    Goes through all transitions and reverses them. It can be seen as reversing
    all directions in a directed graph. Costs are kept the same.

    Args:
        trans: A dictionary containing list of possible transitions and their
            costs for each key that represents the state name.

    Returns:
        A dictionary representing the reversed transitions as given in the
        input args parameter.
    
    """
    
    reverse = {}
    
    for s1 in trans:
        for s2, c in trans[s1]:
            if s2 not in reverse:
                reverse[s2] = set()
            
            reverse[s2].add((s1, c))
    
    return reverse

