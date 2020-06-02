"""



"""


def main():
    """Main method that is run.

    Main method that takes command line arguments and performs given
    operation/s.
    
    """
    from argparse import ArgumentParser
    from data_loader import get_state_space, get_heuristic
    from search import BFS, UCS, DFS, lDFS, IDS, GBFS, HCS, AStar
    from heuristic_check import is_optimistic, is_consistent
    from puzzle_heuristic import manhattan_distance
    
    parser = ArgumentParser('run specified search algorithm on a given state space')
    parser.add_argument('ss', type=str, help='path to a state space to use')
    parser.add_argument('-a', '--algorithm', type=str, choices= ['bfs', 'ucs', 'dfs', 'ldfs', 'ids', 'gbfs', 'hcs', 'astar'], help='state space search algoritm to use')
    parser.add_argument('-d', '--depth', type=int, help='maximum depth for the limited DFS')
    parser.add_argument('-e', '--heuristic', type=str, help='heuristic to use: [path, \'l1\']')
    parser.add_argument('-c', '--check', action='store_true', help="run checks on heuristic")

    args = parser.parse_args()
    
    s0, transitions, goal = get_state_space(args.ss)
    
    heuristic = None
    if args.heuristic:
        if args.heuristic == 'l1':
            heuristic = manhattan_distance(goal)
        else:
            heuristic = get_heuristic(args.heuristic)
    
    if args.algorithm:
        if args.algorithm == 'bfs':
            BFS(s0, transitions, goal)
        elif args.algorithm == 'ucs':
            UCS(s0, transitions, goal)
        elif args.algorithm == 'dfs':
            DFS(s0, transitions, goal)
        elif args.algorithm == 'ldfs':
            if args.depth:
                lDFS(s0, transitions, goal, args.depth)
            else:
                print('Maximum depth not provided.')
        elif args.algorithm == 'ids':
            IDS(s0, transitions, goal)
        elif heuristic:
            if args.algorithm == 'gbfs':
                GBFS(s0, transitions, goal, heuristic)
            elif args.algorithm == 'hcs':
                HCS(s0, transitions, heuristic)
            elif args.algorithm == 'astar':
                AStar(s0, transitions, goal, heuristic)
            else:
                print('Invalid algorithm.')
        else:
            print('No heuristic provided.')
    
    if args.check:
        if heuristic:
            print('Checking heuristic')
            is_optimistic(heuristic, transitions, goal)
            is_consistent(heuristic, transitions)
        else:
            print('No heuristic provided.')


# run if program is called as main program
if __name__ == '__main__':
    main()

