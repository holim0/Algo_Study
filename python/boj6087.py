from collections import deque

w, h = map(int, input().split())


arr = []

link = []

check = [[987654321 for _ in range(w)] for _ in range(h)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

dir = {
    0: "down",
    1: "up",
    2: "left",
    3: "right"
}

for i in range(h):
    s = input()
    s = list(s)
    arr.append(s)

for i in range(h):
    for j in range(w):
        if arr[i][j] == "C":
            link.append((i, j))

sx, sy = link[0]

ex, ey = link[1]

q = deque([(sx, sy, -1, 0)])

check[sx][sy] = 0


def check_Range(x, y):
    global w, h

    if x >= 0 and x < h and y >= 0 and y < w:
        return True
    else:
        return False


answer = 987654321

while q:
    cx, cy, direction, curveCnt = q.popleft()

    if cx == ex and cy == ey:
        answer = min(answer, curveCnt)

    for i in range(4):
        nx, ny = cx+dx[i], cy+dy[i]
        tmp = curveCnt
        ndir = dir[i]
        if check_Range(nx, ny) and (arr[nx][ny] == "." or arr[nx][ny] == "C"):

            if direction == -1:
                q.append((nx, ny, ndir, 0))
                check[nx][ny] = 0

            else:
                if ndir != direction:
                    tmp += 1

                if check[nx][ny] >= tmp:
                    check[nx][ny] = tmp
                    q.append((nx, ny, ndir, tmp))


print(answer)
