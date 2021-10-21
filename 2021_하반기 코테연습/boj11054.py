n = int(input())

number = list(map(int, input().split()))

size = len(number)

left_dp = [1 for _ in range(size)]
right_dp = [1 for _ in range(size)]


for i in range(size):
    for j in range(i):
        if number[i]>number[j]:
            left_dp[i] = max(left_dp[i], left_dp[j]+1)

for i in range(size-1, -1, -1):
    for j in range(i+1, size):
        if number[i]>number[j]:
            right_dp[i] = max(right_dp[i], right_dp[j]+1)
answer = 0
for i in range(size):
    answer = max(answer, right_dp[i]+left_dp[i]-1)

print(answer)
