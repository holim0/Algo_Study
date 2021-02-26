n = int(input())

number = list(map(int, input().split()))

dp = number[:]


for i in range(1, len(number)):

    cur = number[i]

    for j in range(i):

        if number[j] < cur:

            dp[i] = max(dp[i], dp[j]+cur)

print(max(dp))
