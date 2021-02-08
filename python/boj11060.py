N = int(input())

miro = list(map(int, input().split()))

dp = [1005 for _ in range(N)]

dp[0] = 0
for i in range(1, N):
    for j in range(i):
        if miro[j] >= i-j:
            dp[i] = min(dp[i], dp[j]+1)


if dp[-1] == 1005:
    print(-1)

else:
    print(dp[-1])
