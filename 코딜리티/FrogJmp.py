import math


def solution(X, Y, D):

    if Y-X == 0:
        return 0

    dist = Y-X

    val = int(dist/D)

    if dist % D == 0:
        return val

    else:
        return val+1
