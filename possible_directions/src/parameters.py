# Target Function f(x)->min 
f = lambda arg: arg[2]
# Restrictions (mean with >= sign)
g = [
    lambda arg: -arg[0]**2 - 2 * arg[0] * arg[1] - 2 * arg[1]**2 + 2 * arg[0] + arg[1] + arg[2] + 2,
    lambda arg: -arg[0]**2 - arg[1]**2 + arg[0] - arg[1] + arg[2] + 3,
    lambda arg: -arg[0]**2 - arg[0] + 4 * arg[1] + arg[2] - 3
]
# Dimension
n = 3
# Gradients
f_grad = [0, 0, 1]
g_grad = [
    [
        lambda arg: -2 * arg[0] - 2 * arg[1] + 2,
        lambda arg: 2 * arg[0] - 4 * arg[1] + 1,
        1
    ],
    [
        lambda arg: -2 * arg[0] + 1,
        lambda arg: -2 * arg[1] - 1,
        1
    ],
    [
        lambda arg: -2 * arg[0] - 1,
        4,
        1
    ]
]
# Start Point x0
x0 = (0, 1, 2.5)
# Using |x(k) - x(k-1)| < eps measure to stop the algorithm
eps = 0.05