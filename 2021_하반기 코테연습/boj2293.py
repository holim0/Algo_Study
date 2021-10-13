n, k = map(int, input().split())

coin = []
dp = [0 for _ in range(k+1)]

for _ in range(n):
    c = int(input())
    coin.append(c)

dp[0]=1


for c in coin:
    for i in range(1, k+1):
        if i-c>=0:
            dp[i] +=dp[i-c]



print(dp[k])
