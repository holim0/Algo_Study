import sys
import heapq

v, e  = map(int, input().split())

k = int(input())
INF = sys.maxsize
g = [[]* v for _ in range(v)]

dist = [INF for _ in range(v)]

dist[k-1]=0

for i in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    g[u-1].append((w, v-1))



q = []

heapq.heappush(q, (0, k-1))


while q:
    cur_w, cur = heapq.heappop(q)

    if dist[cur] < cur_w:
        continue

    for i in range(len(g[cur])):
        next_dist, next_val  = g[cur][i]
        tmp_dist = cur_w + next_dist
        if tmp_dist < dist[next_val]:
            dist[next_val] = tmp_dist
            heapq.heappush(q, (tmp_dist,next_val))


for d in dist:
    if d==INF :
        print("INF")

    else:
        print(d)
