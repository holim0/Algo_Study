n = int(input())

link = []

for i in range(n):
    a, b = map(int, input().split())
    link.append((a, b))

link.sort()

r_dp = [0 for _ in range(500+1)]
l_dp = [0 for _ in range(500+1)]


for l in link:
    a, b = l

    l_dp[a] = max(r_dp[:b]) +1
    r_dp[b] = l_dp[a]


print(n-max(l_dp))