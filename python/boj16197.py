import sys
sys.setrecursionlimit(10**7)


N, M = map(int, input().split())

board = [0 for _ in range(N)]

for i in range(N):
    board[i] = list(input())


pos = []
for i in range(N):
    for j in range(M):
        if board[i][j] == "o":
            pos.append([i, j])


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

answer = 9987654321


def checkRange(x, y):
    global N, M

    if x >= 0 and x < N and y >= 0 and y < M:
        return True
    return False


def dfs(x1, y1, x2, y2, click):
    global answer, dx, dy, board

    if click > 10:
        answer = min(answer, click)
        return

    if answer < click:
        return

    for i, j in zip(dx, dy):
        nx1, ny1 = x1+i, y1+j
        nx2, ny2 = x2+i, y2+j

        if not checkRange(nx1, ny1) and not checkRange(nx2, ny2):
            continue
        elif checkRange(nx1, ny1) and not checkRange(nx2, ny2):
            answer = min(answer, click+1)
            continue
        elif not checkRange(nx1, ny1) and checkRange(nx2, ny2):
            answer = min(answer, click+1)
            continue

        else:
            if board[nx1][ny1] == "#":
                nx1, ny1 = x1, y1

            if board[nx2][ny2] == "#":
                nx2, ny2 = x2, y2

        dfs(nx1, ny1, nx2, ny2, click+1)


dfs(pos[0][0], pos[0][1], pos[1][0], pos[1][1], 0)


if answer > 10:
    print(-1)

else:
    print(answer)
