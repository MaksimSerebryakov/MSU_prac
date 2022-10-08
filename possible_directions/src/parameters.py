# Target Function f(x)->min 
f = lambda arg: (arg[0] - 3) ** 2 + (arg[1] - 3) ** 2
# Restrictions (mean with >= sign)
g = [
    lambda arg: 2*arg[0] - arg[1]**2 - 1,
    lambda arg: 9 - 0.8*arg[0] - 2*arg[1]
]
# Dimension
n = 2 
# Gradients
f_grad = [lambda arg: 2*(arg[0] - 3), lambda arg: 2*(arg[1] - 3)]
g_grad = [
    [
        2,
        lambda arg: -2*arg[1]
    ],
    [
        lambda arg: -1.6*arg[0],
        -2
    ]
]
# Start Point x0
x0 = (3, -1)
# Using |x(k) - x(k-1)| < eps measure to stop the algorithm
eps = 0.0001