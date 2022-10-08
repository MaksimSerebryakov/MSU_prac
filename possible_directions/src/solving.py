import numpy as np

from scipy import optimize
from .handlers import *
from math import *

class linear_prog_problem:
    def __init__(self, grad_f, grad_g):
        self.c_ = [0] * (n + 1)
        self.c_[-1] = -1
        self.a_ub = [
            np.append(grad_f, 1)
        ]
        for grad in grad_g:
            self.a_ub.append(np.append(grad, -1) * (-1))
        self.b_ub = np.array([0]*(1 + len(grad_g)))
        self.bounds = [(-1, 1)] * (n + 1)
        self.bounds[-1] = (None, None)
        print(self.c_, self.a_ub, self.b_ub, self.bounds, sep='\n')
    
    def solve_lpp(self):
        return optimize.linprog(c=self.c_, A_ub=self.a_ub, b_ub=self.b_ub, bounds=self.bounds)


def main_algorithm():
    if check_start_point():
        print("it's okey")
    else:
        print('x0 does not belong to scope of permissible values')
        return None
    
    x_prev = x0
    x_cur = [x + eps*10 for x in x0]
    
    while points_dist(x_prev, x_cur) >= eps:
        grad_f_x_prev = np.array([])
        grad_g_x_prev = []

        # Finding gradients for f and g's
        for elem in f_grad:
            if callable(elem):
                grad_f_x_prev = np.append(grad_f_x_prev, elem(x_prev))
            else:
                grad_f_x_prev = np.append(grad_f_x_prev, elem)
        g_len = len(g)
        for j in range(g_len):
            if g[j](x_prev) != 0:
                continue
            grad = []
            for i in range(n):
                if callable(elem[i]):
                    grad.append(elem[i](x_prev))
                else:
                    grad.append(elem[i])
            grad_g_x_prev.append(grad)
        
        lpp = linear_prog_problem(grad_f_x_prev, grad_g_x_prev)
        res = lpp.solve_lpp()
        print(res.x)
        break