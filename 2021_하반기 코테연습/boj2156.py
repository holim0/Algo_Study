n = int(input())

g = [0 for _ in range(n+1)]

for i in range(1, n+1):
    tmp= int(input())
    g[i] = tmp



dp = [0 for _ in range(n+1)]

dp[1] = g[1]

if n>1:
    dp[2] = g[1] + g[2]



for i in range(3, n+1):
    dp[i] = max(dp[i-3]+g[i]+g[i-1], dp[i-2]+g[i], dp[i-1])



print(dp[n])