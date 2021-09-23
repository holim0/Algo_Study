import heapq
n, k = map(int, input().split())

STAD = 100000
INF = 987654321

visit = [INF for _ in range(100000+5)]

answer = -1

visit[n] = 0

q= []

heapq.heappush(q, (0, n))

while q:
    time, cur = heapq.heappop(q)
    
    if cur==k:
        answer = visit[cur]
        break
    

    if 2*cur<=STAD and time < visit[2*cur]:
        visit[2*cur] = time
        heapq.heappush(q, (time, 2*cur))

    if cur+1<=STAD and time+1 < visit[cur+1]:
        visit[cur+1] = time+1
        heapq.heappush(q, (time+1, cur+1))
    
    if cur-1>=0 and time+1 < visit[cur-1]:
        visit[cur-1] = time+1
        heapq.heappush(q, (time+1, cur-1))
    
    
print(answer)

