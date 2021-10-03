from heapq import *
import sys
from collections import defaultdict

input = sys.stdin.readline

answer = 0

v,e = map(int, input().split())

link = defaultdict(list)


for _ in range(e):
    a, b, c = map(int, input().split())
    link[a].append((b,c))
    link[b].append((a, c))

link_set = []

h = []


heappush(h, (0, 1))
cnt = 0
while h:
    weight, cur = heappop(h)

    if cur not in link_set:
        link_set.append(cur)
        answer+=weight


        for nxt in link[cur]:
            n, nw = nxt
            if n not in link_set:
                heappush(h, (nw, n))

print(answer)