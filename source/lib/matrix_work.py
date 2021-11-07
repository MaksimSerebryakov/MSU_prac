import numpy as np

def saddle_point(a):
    a = np.array(a)
    maximin = np.max(np.min(a, axis=1))
    minimax = np.min(np.max(a, axis=0))

    if minimax == maximin:
        i = np.where(np.min(a, axis=1) == maximin)[0][0]
        j = np.where(np.max(a, axis=0) == minimax)[0][0]

        return i, j
    return None, None