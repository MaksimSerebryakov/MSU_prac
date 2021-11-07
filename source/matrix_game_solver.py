import sys

import lib.matrix_work 

def input_matrix():
    print('Input source data:')
    try:
        m = int(input('Number of strategies of player 1: '))
        n = int(input('Number of strategies of player 2: '))
        print()

        print('Enter the game matrix')

        matrix = []

        for i in range(m):
            row = input().split()

            assert len(row) == n
            
            matrix.append([float(j) for j in row])
    except AssertionError:
        print('Wrong number of column')
        sys.exit()

    return m, n, matrix

m, n, matrix = input_matrix()

