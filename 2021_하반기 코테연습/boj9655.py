n = int(input())

dp =[-1 for _ in range(n+1)]

## 1은 sk, 0은 cy


if n==1:
    print("SK")
    exit(0)

dp[0] = False
dp[1] = True
dp[2] = False

for i in range(3, n+1):
    dp[i] = not dp[i-3]

if dp[n]:
    print("SK")
else:
    print("CY")