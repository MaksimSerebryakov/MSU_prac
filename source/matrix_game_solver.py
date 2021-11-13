import sys

from . import matrix_work
import numpy as np
import matplotlib.pyplot as plt

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

    return matrix

def input_matrix_from_file(f_name):
    matrix = np.loadtxt(f_name)
    n = len(matrix[0])
    m = len(matrix)

    try:
        for i in range(1, m):
            assert len(matrix[i]) == n
    except AssertionError:
        print('Wrong matrix shape')
        sys.exit()

    return matrix

def nash_equilibrium(a):
    a = np.array(a)
    i, j = matrix_work.saddle_point(a)
    if i != None:
        print("There is a solution in pure strategies for both players:")
        print("Optimal strategy for the 1st player: ", end='')
        print([*a[i]])
        print("Optimal strategy for the 2nd player: ", end='')
        print([*a[:, j]])
        print("Game value: {}".format(a[i][j]))
        return a[i][j], a[i], a[:, j]

    try:    
        target_f, p, q = matrix_work.simplex_method(a)

        assert target_f != None
    except AssertionError:
        print("Simplex method didn't succeed to find an optimal solution")
        sys.exit()
    
    print("There is a solution in mixed strategies: ")
    print("Optimal strategy for the 1st player: ", end='')
    print_strategy(p)
    print("Optimal strategy for the 2nd player: ", end='')
    print_strategy(q)
    print("Game value: ", end='')
    print("%.4f" %target_f)

    return target_f, p, q

def vizualization(p, num):
    plt.title("Визуализация вектора оптимальной стратегии {}-го игрока".format(num))
    x = np.linspace(1, len(p), num=len(p)) 
    plt.axis([0, len(p) + 1, 0, max(p) + 1/2]) 
    plt.style.use('ggplot')
    plt.stem(x, p, basefmt=' ')
    plt.show()

def print_strategy(p):
    print('[', end=' ')
    for s in p:
        print("%.4f" %s, end=' ')
    print(']')
