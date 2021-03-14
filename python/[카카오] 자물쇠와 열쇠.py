import copy
import sys

sys.setrecursionlimit(10**6)

flag = False


def turn(key):
    size = len(key)
    tmp = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            tmp[j][size-1-i] = key[i][j]

    return tmp


def getSol(sx, sy, back_len, turn_key, lock):

    size = len(turn_key)
    back = [[0] * (back_len+1) for _ in range(back_len+1)]

    for i in range(len(lock)):
        for j in range(len(lock)):
            back[i+size][j+size] = lock[i][j]

    for i in range(size):
        for j in range(size):
            back[i+sx][j+sy] += turn_key[i][j]

    for i in range(len(lock)):
        for j in range(len(lock)):
            if back[i+size][j+size] != 1:
                return False

    return True


def solution(key, lock):

    global flag

    n = len(lock)
    m = len(key)

    copy_key = copy.deepcopy(key)
    back_len = 2*(m-1) + n
    for i in range(4):
        turn_key = turn(copy_key)

        for i in range(0, m+n):
            for j in range(0, m+n):
                if getSol(i, j, back_len, turn_key, lock):
                    return True

        copy_key = copy.deepcopy(turn_key)

    return False
