n, k = map(int, input().split())


coin = []
max_val = 100000 + 5
dp = [max_val for _ in range(max_val)]

for i in range(n):
    c = int(input())
    coin.append(c)
    dp[c] = 1

for i in range(1, k+1):
    curCoin = i

    if curCoin in coin:
        dp[curCoin] = 1
    else:
        for c in coin:
            if c < curCoin:
                dp[curCoin] = min(dp[curCoin], dp[curCoin-c]+1)


if dp[k] == max_val:
    print(-1)
else:
    print(dp[k])
