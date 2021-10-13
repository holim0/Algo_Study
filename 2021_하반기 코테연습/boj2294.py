n, k = map(int, input().split())

INF = 1e10

coin = []

for _ in range(n):
    c = int(input())
    coin.append(c)

dp = [INF for _ in range(k+1)]

dp[0]=0

for c in coin:
    
    for i in range(1, k+1):
        if i-c>=0:
            dp[i] = min(dp[i], dp[i-c]+1)

if dp[k]==INF:
    print(-1)
else:
    print(dp[k])