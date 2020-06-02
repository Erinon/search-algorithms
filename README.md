# search-algorithms
A CLI program that performs various path-finding algorithms. State space where the search is performed is given as a .txt file. Program is also able to perform checks whether the heuristic is optimistic and/or consistent. Some heuristics are available also as .txt files and manhattan distance heuristics for 8-puzzle is implemented as a function. It is possible to easily add new heuristic functions.

## Algorithms
Currently available algorithms are breadth-first search, uniform-cost search, depth-first search, limited depth-first search, iterative deepening search, greedy best-first search, hill climb search and A* search.


## Usage
The basic usage can be checked with:
    
    python3 main.py -h

To check if and how the program works, it can be for example run with:
    
    python3 main.py maps/3x3_puzzle.txt  -a astar -e maps/3x3_misplaced_heuristic.txt -c

