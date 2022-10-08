import src.solving as solve
"""from scipy import optimize
import numpy as np

c = np.array([0, 0, -1])
a_ub = np.matrix([
    [0, -4.2, 1],
    [4.8, 2, 1]
])
bub = np.array([0, 0])
d1_bounds = (-1, 1)
d2_bounds = (-1, 1)
teta_bounds = (None, None)

res = optimize.linprog(c, A_ub=a_ub, b_ub=bub, bounds=[d1_bounds, d2_bounds, teta_bounds])

print(res.x)"""
if __name__ == "__main__":
    print('Please, edit file "src/parameters.py according to your problem"')
    print()
    
    solve.main_algorithm()