import sys
n, m = map(int, input().split())

game = []

visit = [[False] * m for _ in range(n)]
tx, ty = 0, 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
    s = sys.stdin.readline()
    s = s.rstrip("\n")
    game.append(list(s))


def check_range(x, y):
    if x >= 0 and x < n and y >= 0 and y < m:
        return True

    return False


def check_rotate(curx, cury, cnt):
    global visit, tx, ty

    if curx == tx and cury == ty and cnt >= 4:
        print("Yes")
        exit(0)

    for i in range(4):
        nx, ny = curx+dx[i], cury+dy[i]

        if check_range(nx, ny) and game[nx][ny] == game[curx][cury]:
            if not visit[nx][ny]:
                visit[nx][ny] = True
                check_rotate(nx, ny, cnt+1)
                visit[nx][ny] = False


if __name__ == "__main__":
    for i in range(n):
        for j in range(m):
            visit = [[False] * m for _ in range(n)]
            tx, ty = i, j
            check_rotate(i, j, 0)


print("No")
