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
    
    def solve_lpp(self):
        return optimize.linprog(c=self.c_, A_ub=self.a_ub, b_ub=self.b_ub, bounds=self.bounds)


def main_algorithm():
    if check_start_point():
        print("Start point belongs to scope of permissible values")
    else:
        print('x0 does not belong to scope of permissible values')
        raise Exception
    
    x_prev = x0
    x_cur = [x + eps*10 for x in x0]
    fl = True
    
    while points_dist(x_prev, x_cur) >= eps:
        if fl:
            fl = False
        else:
            x_prev = x_cur

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
            if abs(g[j](x_prev) > 0.005):
                continue
            grad = []
            for i in range(n):
                if callable(g_grad[j][i]):
                    grad.append(g_grad[j][i](x_prev))
                else:
                    grad.append(g_grad[j][i])
            grad_g_x_prev.append(grad)
        
        lpp = linear_prog_problem(grad_f_x_prev, grad_g_x_prev)
        res = lpp.solve_lpp()
        if res.status != 0:
            return x_prev + alpha_step, f(x_prev + alpha_step)
        elif res.x[-1] < 0:
            return x_prev + alpha_step, f(x_prev + alpha_step)
        else:
            d_vec = np.array(res.x[0:-1])
            # We should solve g(a) inequation so I'm going check 
            # all alpha values from 0 to alpha bound
            alpha_step = 0.00001
            alpha = 1000000000000000

            for elem in g:
                alpha_cur = alpha_step
                x_cur = np.array(x_prev) + d_vec*alpha_cur

                while elem(x_cur) >= 0:
                    alpha_cur += alpha_step
                    x_cur = np.array(x_prev) + d_vec*alpha_cur
                x_cur = np.array(x_prev) + d_vec*(alpha_cur - 2 * alpha_step)


                if alpha_cur < alpha:
                    alpha = alpha_cur
                    
            x_cur = np.array(x_prev) + d_vec*alpha

            if points_dist(x_cur, x_prev) < eps:
                print(x_cur)
                return x_cur, f(x_cur)
