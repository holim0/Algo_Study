import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append([0, 0, 1])
    check = [[[0] * 2 for i in range(m)] for i in range(n)]
    check[0][0][1] = 1
    while q:
        cx, cy, b = q.popleft()
        if cx == n - 1 and cy == m - 1:
            return check[cx][cy][b]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if s[nx][ny] == 1 and b == 1:
                    check[nx][ny][0] = check[cx][cy][1] + 1
                    q.append([nx, ny, 0])
                elif s[nx][ny] == 0 and check[nx][ny][b] == 0:
                    check[nx][ny][b] = check[cx][cy][b] + 1
                    q.append([nx, ny, b])
    return -1


n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, list(input().strip()))))
print(bfs())
