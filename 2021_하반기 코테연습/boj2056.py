from collections import deque

n = int(input())

answer = 0

degree = [0 for _ in range(n+1)]

link = [[] for _ in range(n+1)]

need_time = [0 for _ in range(n+1)]

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    info = list(map(int, input().split()))

    degree[i]+=info[1]
    need_time[i] = info[0]

    for j in range(2, len(info)):
        cur = info[j]
        link[cur].append(i)

q =deque([])


for i in range(1, n+1):
    if degree[i]==0:
        dp[i] = need_time[i]
        q.append((i, need_time[i]))



while q:
    cur, time = q.popleft()

   
    for nxt in link[cur]:
        degree[nxt]-=1
        dp[nxt] = max(dp[nxt], dp[cur]+need_time[nxt])
        if degree[nxt]==0:
            q.append((nxt, need_time[nxt]))

for d in dp:
    answer = max(answer, d)
    
    
print(answer)

