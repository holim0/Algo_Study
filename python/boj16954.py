import sys
import copy
from collections import deque

chess = []


dx = [0, 0, 0, 1, -1, 1, -1, 1, -1]

dy = [0, -1, 1, 0, 0, 1, -1, -1, 1]

sx, sy = 7, 0

target_x, target_y = 0, 7

for i in range(8):
    s = input()
    chess.append(list(s))

visit = [[[False for _ in range(10)] for _ in range(10)] for _ in range(10)]
q = deque([(sx, sy, 0)])


visit[sx][sy][0] = True


def check_range(x, y):
    if x >= 0 and x < 8 and y >= 0 and y < 8:
        return True
    return False


flag = False
while q:
    curx, cury, time = q.popleft()

    if curx == target_x and cury == target_y:
        flag = True
        break

    for i in range(0, 9):
        nx, ny = curx+dx[i], cury+dy[i]
        nt = min(time+1, 8)

        if not check_range(nx, ny):
            continue

        if nx-time-1 >= 0 and chess[nx-time-1][ny] == "#":
            continue

        if nx-time >= 0 and chess[nx-time][ny] == "#":
            continue

        if not visit[nx][ny][nt]:
            visit[nx][ny][nt] = True
            q.append((nx, ny, nt))


if flag:
    print(1)
else:
    print(0)
