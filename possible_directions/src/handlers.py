from xmlrpc.client import Boolean
from .parameters import *
def print_smth():
    print(f(x0))
    print(g_grad[1][0](x0), g_grad[1][1])

def check_start_point():
    for rest in g:
        if rest(x0) < 0:
            return False
    
    return True

def points_dist(x1, x2):
    dist = 0
    for i in range(n):
        dist += (x1[i] - x2[i])**2
    
    return dist**0.5