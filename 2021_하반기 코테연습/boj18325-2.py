import heapq

answer= []
INF = 987654321

n, m, k, x = map(int, input().split())

link= [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    link[a].append((b, 1))


dist = [INF for _ in range(n+1)]

dist[x] = 0

q = []

heapq.heappush(q, (0, x))

while q:
    cur_d, cur = heapq.heappop(q)

    if dist[cur] < cur_d: continue


    for n in link[cur]:
        nxt, d = n[0], n[1]
        
        next_dist = cur_d + d
        
        if next_dist < dist[nxt]:
            dist[nxt] = next_dist
            heapq.heappush(q, (next_dist, nxt))



for idx in range(len(dist)):
    if dist[idx]==k:
        answer.append(idx)






if len(answer) ==0:
    print(-1)

else:
    answer.sort()
    for a in answer:
        print(a, end="\n")



