import sys
input = sys.stdin.readline
a = input()
b = input()

a_size = len(a)-1
b_size = len(b)-1
dp = [[0] * (a_size+1) for _ in range(b_size+1)]


for i in range(b_size):
    for j in range(a_size):
        if b[i] == a[j]:
            dp[i+1][j+1] = dp[i][j]+1

        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

longest = dp[-1][-1]

common = list()

check_range = a_size+1
target = longest
for i in reversed(range(b_size+1)):
    for j in range(check_range):
        if dp[i][j] != dp[i-1][j-1] and dp[i][j] != dp[i-1][j] and dp[i][j] != dp[i][j-1] and dp[i][j] == target:
            common.append(b[i-1])
            check_range = j
            target -= 1
            break

reversed_str = common[::-1]

print(longest)
if longest:
    print("".join(reversed_str))
