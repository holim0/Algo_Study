from collections import defaultdict
import sys
import heapq

input = sys.stdin.readline


n, m = map(int, input().split())


enter_cnt = [0 for _ in range(n+1)]
link = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    enter_cnt[b]+=1


answer = []
h = []

for i in range(1, len(enter_cnt)):
    if enter_cnt[i]==0:
        heapq.heappush(h, i)



for _ in range(1, len(enter_cnt)):
    cur = heapq.heappop(h)
    
    
    if enter_cnt[cur] == 0:
        answer.append(cur)
        for j in link[cur]:
            enter_cnt[j]-=1
            if enter_cnt[j]==0:
                heapq.heappush(h, j)
        

for a in answer:
    print(a, end=" ")


        


