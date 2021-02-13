n, m = map(int, input().split())


arr = []

dx = [-1, 0, -1]
dy = [0, -1, -1]


for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

check = [[False] * m for _ in range(n)]

dp = [[0] * m for _ in range(n)]


def checkRange(x, y):
    global n, m

    if x >= 0 and x < n and y >= 0 and y < m:
        return True

    return False


for i in range(n):
    for j in range(m):
        value = -1

        for x, y in zip(dx, dy):
            nx, ny = i+x, j+y
            if checkRange(nx, ny):
                value = max(value, dp[nx][ny])

        if value == -1:
            dp[i][j] = arr[i][j]
        else:
            dp[i][j] = arr[i][j]+value


print(dp[-1][-1])
