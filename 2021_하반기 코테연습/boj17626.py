n = int(input())

answer = 0

squ = []

k = 1

while k*k<=n:
    squ.append(k*k)
    k+=1

INF = 1e10

dp = [INF for _ in range(n+1)]

dp[0]=0

for i in range(1, n+1):
    for s in squ:
        if i-s>=0:
            if dp[i] > dp[i-s]+1:
                dp[i] = dp[i-s]+1
            

print(dp[n])