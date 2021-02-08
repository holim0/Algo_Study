import sys
from collections import deque


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
directionList = [1, 2, 3, 4]
answer = sys.maxsize


def checkRange(x, y, N):

    if x >= 0 and x < N and y >= 0 and y < N:
        return True

    return False


def bfs(x, y, cost, d, size, board):

    global answer
    check = [[0] * size for _ in range(size)]
    deq = deque([(x, y, cost, d)])

    while deq:
        cx, cy, money, direction = deq.popleft()

        if cx == size-1 and cy == size-1:
            answer = min(answer, money)

        for i, j, k in zip(dx, dy, directionList):

            nx, ny = cx+i, cy+j

            if checkRange(nx, ny, size) and board[nx][ny] == 0:

                new_cost = money

                if direction == k:
                    new_cost += 100

                else:
                    new_cost += 600

                if not check[nx][ny] or check[nx][ny] > new_cost:
                    check[nx][ny] = new_cost
                    deq.append((nx, ny, new_cost, k))


def solution(board):
    global answer

    size = len(board)

    bfs(0, 0, 0, 1, size, board)

    bfs(0, 0, 0, 4, size, board)

    return answer
