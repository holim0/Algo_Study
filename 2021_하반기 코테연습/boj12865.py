n, k = map(int, input().split())

info = [0 for _ in range(n+1)]

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
    w, v  = map(int, input().split())
    info[i]= (w, v)


for i in range(1, n+1):
    for j in range(1, k+1):
        w, v = info[i]
        if j-w>=0: 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]


print(dp[n][k])