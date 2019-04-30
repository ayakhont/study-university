import numpy as np
import sys

def fibDynamic(n):
    if n <= 1:
        return n
    else:
        f = np.zeros(n, int)
        f[0] = 1
        f[1] = 1
        for i in range(2, n):
            f[i] = f[i-1] + f[i-2]
            n = f[i]
    return n


def fibRecursive(n):
    if n <= 1:
        return n
    return fibRecursive(n-1) + fibRecursive(n-2)


if __name__ == "__main__":
    number = 10

    for i in range(number):
        print(fibRecursive(i))

    for i in range(number):
        print(fibDynamic(i))