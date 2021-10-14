import heapq as hq

n, m = map(int, input().split())

answer = []

degree = [0 for _ in range(n+1)]
link = [[] for _ in range(n+1)]



for _ in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    degree[b]+=1

q = []

for i in range(1, n+1):
    if degree[i]==0:
        hq.heappush(q, i)

while q:
    cur = hq.heappop(q)

    answer.append(cur)

    for nxt in link[cur]:
        degree[nxt]-=1

        if degree[nxt]==0:
            hq.heappush(q, nxt)

for a in answer:
    print(a, end=" ")   