c, n = map(int, input().split())

mapp = []

INF = 1e10

for _ in range(n):
    cost, people = map(int, input().split())
    mapp.append((cost, people))

dp = [INF for _ in range(1101)]

dp[0] = 0



for m in mapp:
    
    cost, customer = m

    for i in range(customer, 1101):

        dp[i] = min(dp[i], dp[i-customer]+cost)


answer = 1e10


for i in range(c, 1101):
    answer = min(answer, dp[i])

print(answer)