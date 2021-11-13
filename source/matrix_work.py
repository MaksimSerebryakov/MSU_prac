import numpy as np
from scipy.optimize import linprog

def saddle_point(a):
    a = np.array(a)
    maximin = np.max(np.min(a, axis=1))
    minimax = np.min(np.max(a, axis=0))

    if minimax == maximin:
        i = np.where(np.min(a, axis=1) == maximin)[0][0]
        j = np.where(np.max(a, axis=0) == minimax)[0][0]

        return i, j
        
    return None, None

def simplex_method(a):
    a = np.array(a)
    min_el = min(0, np.min(a))
    a += abs(min_el)

    second = a
    first = np.copy(np.transpose(second))

    m = len(a)
    n = len(a[0])

    first *= -1
    b_first = np.array([-1] * n)
    c_first = np.array([1] * m)
    b_second = np.array([1] * m)
    c_second = np.array([-1] * n)
    bound = (0, None)

    res_first = linprog(c_first, b_ub=b_first, A_ub=first, bounds=bound, method='simplex')
    res_second = linprog(c_second, b_ub=b_second, A_ub=second, bounds=bound, method='simplex')

    if res_first.success and res_second.success:
        target_f = 1 / res_first.fun
        P = np.array(res_first.x) * target_f
        Q = np.array(res_second.x) * target_f
        target_f -= abs(min_el)

        return target_f, P, Q
    else:
        return None, None, None
