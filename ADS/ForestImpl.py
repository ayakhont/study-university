import numpy as np


def init_forest(n: int):
    parents_array = np.array(n)
    for i in range(n):
        parents_array[i] = i
    rang_array = np.array(np.zeros(n), int)

    return parents_array, rang_array

