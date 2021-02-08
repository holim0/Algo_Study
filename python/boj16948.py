from collections import deque

N = int(input())

pos = list(map(int, input().split()))

r1, c1, r2, c2 = pos[0], pos[1], pos[2], pos[3]


dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]


def checkRange(x, y, N):
    if x >= 0 and x < N and y >= 0 and y < N:
        return True
    else:
        return False


q = deque([(r1, c1, 0)])

answer = 0

check = [[False] * N for _ in range(N)]
check[r1][c1] = True


while q:
    cx, cy, cnt = q.popleft()

    if cx == r2 and cy == c2:
        answer = cnt
        break

    for i, j in zip(dx, dy):
        nx, ny = cx+i, cy+j

        if checkRange(nx, ny, N) and check[nx][ny] == False:
            check[nx][ny] = True
            q.append((nx, ny, cnt+1))

if answer == 0:
    answer = -1

print(answer)
