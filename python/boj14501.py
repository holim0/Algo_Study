n = int(input())

arr = []
dp = [0 for _ in range(n)]
answer = 0


for i in range(n):
    t, p = map(int, input().split())
    arr.append((t,p))


for i in range(n):
    next = i + arr[i][0]
    if next <= n:
        dp[i] = arr[i][1]



for i in range(len(arr)):
     
    if i==0 and i+arr[i][0]<=n: 
        dp[i] = max(dp[i], arr[i][1])

    else:
        for j in range(i):
            next = arr[j][0] + j

            if next<=i and i + arr[i][0]<=n:
                dp[i] = max(dp[i], dp[j]+ arr[i][1])

print(max(dp))





