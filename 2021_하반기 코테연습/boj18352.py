import heapq

n, m, k, x = map(int, input().split())


link = [[] for _ in range(n+1)]

answer = 0

for i in range(m):
    start, to = map(int, input().split())

    link[start].append((to, 1))

INF = 987654321

dist = [INF for _ in range(n+1)]

dist[x] = 0

q= []
heapq.heappush(q, (0, x))


while q:
    curdist, cur  = heapq.heappop(q)

    if dist[cur] < curdist: continue


    for to in link[cur]:
        new_dist = curdist + to[1]

        if new_dist < dist[to[0]]:
            dist[to[0]] = new_dist
            heapq.heappush(q, (new_dist, to[0]))


answer = []

for i in range(1, n+1):
    if dist[i] == k:
        answer.append(i)

if len(answer)==0:
    print(-1)

else:
    for a in answer:
        print(a, end="\n")