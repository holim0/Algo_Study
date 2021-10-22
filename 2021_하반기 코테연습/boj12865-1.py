n, k = map(int, input().split())

item = [-1, ]

for _ in range(n):
    w, v = map(int, input().split())
    item.append((w, v))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        cur_w, cur_v = item[i]

        if j>=cur_w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cur_w]+cur_v)

        else:
            dp[i][j] = dp[i-1][j]




print(dp[n][k])