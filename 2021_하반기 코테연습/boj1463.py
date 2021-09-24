n = int(input())

INF = 9887654321

dp = [INF for _ in range(n+1)]

dp[n] = 0



for i in range(n, 0, -1):
    
    if i+1<=n:
        dp[i] = dp[i+1]+1

    if i*3<=n:
        dp[i] = min(dp[i], dp[i*3]+1)

    if i*2<=n:
        dp[i] = min(dp[i], dp[i*2]+1)


print(dp[1])







    