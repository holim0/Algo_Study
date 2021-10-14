import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

INF = 1e10

while t:


    n, m, k = map(int, input().split())
    
    link = [[] for _ in range(n+1)]

    for _ in range(k):
        u, v, c, d = map(int, input().split())
        link[u].append((v, c, d))

    
    dist = [[INF for _ in range(m+1)] for _ in range(n+1)]

    dist[1][0] =0
    q = deque([])

    q.append((0, 0, 1))

    while q:
        cur_dist, cur_cost, cur = q.popleft()

        if dist[cur][cur_cost]<cur_dist: continue
        if cur_cost>m: continue


        for l in link[cur]:
            nxt, nxt_cost, nxt_dist = l

            if nxt_cost+cur_cost>m: continue

            if nxt_dist+cur_dist<dist[nxt][nxt_cost+cur_cost]:
                dist[nxt][nxt_cost+cur_cost] = nxt_dist+cur_dist
                q.append((nxt_dist+cur_dist, nxt_cost+cur_cost, nxt))


    if min(dist[n])==INF:
        print("Poor KCM")
    else:
        print(min(dist[n]))



    t-=1