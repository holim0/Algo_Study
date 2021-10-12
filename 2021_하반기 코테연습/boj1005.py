import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

while t:

    n, k = map(int, input().split())

    degree = [0 for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    link = [[] for _ in range(n+1)]
    q = deque([])

    time = list(map(int, input().split()))

    for _ in range(k):
        a, b = map(int, input().split())
        link[a].append(b)
        degree[b]+=1

    w = int(input())

    for i in range(1, n+1):
        if degree[i]==0:
            q.append(i)
            dp[i] = time[i-1]

    while q:
        cur = q.popleft()

        for nxt in link[cur]:
            dp[nxt] = max(dp[nxt], dp[cur]+time[nxt-1])
            degree[nxt]-=1

            if degree[nxt]==0:
                q.append(nxt)

    print(dp[w])
    t-=1