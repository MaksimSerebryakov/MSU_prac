import sys

import lib.matrix_work 

from scipy.optimize import linprog

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

def input_matrix_from_file(f_name):
    f = open(f_name, 'r')

    matrix = []

    for line in f:
        row = line.split()

        matrix.append([float(j) for j in row])

    return len(matrix), len(matrix[0]), matrix

matrix = [[4, 0, 6, 2, 2, 1], [3, 8, 4, 10, 4, 4], [1, 2, 6, 5, 0, 0], [6, 6, 4, 4, 10, 3], [10, 4, 6, 4, 0, 9], [10, 7, 0, 7, 9, 8]]

f, p, q = lib.matrix_work.simplex_method(matrix)

print(f, p, q, sep='\n')