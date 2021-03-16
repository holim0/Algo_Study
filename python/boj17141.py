import sys
from collections import deque
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = [0 for _ in range(n)]

virus_location = []

for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            virus_location.append((i, j))


virus_johab = list(combinations(virus_location, m))

time = 987654321


def check_range(x, y):
    global n

    if x >= 0 and x < n and y >= 0 and y < n:
        return True

    return False


def check_done(arr, visit):
    global n
    for i in range(n):
        for j in range(n):
            if (arr[i][j] == 0 or arr[i][j] == 2) and visit[i][j] == False:
                return False

    return True


for virus_list in virus_johab:

    visit = [[False] * n for _ in range(n)]
    q = deque([])
    for virus in virus_list:
        x, y = virus
        q.append((x, y, 0))
        visit[x][y] = True

    if check_done(arr, visit):
        time = min(time, 0)

    while q:
        cx, cy, ct = q.popleft()
        # print("cur", cx, cy, ct)

        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if check_range(nx, ny) and not visit[nx][ny] and arr[nx][ny] != 1:
                visit[nx][ny] = True
                q.append((nx, ny, ct+1))
        if check_done(arr, visit):
            time = min(time, ct+1)

if time == 987654321:
    print(-1)
else:
    print(time)
