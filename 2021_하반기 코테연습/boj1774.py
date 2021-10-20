import heapq as hp
import math
n, m = map(int, input().split())

check = [False for _ in range(n+1)]

link =[[] for _ in range(n+1)]
mst = set()

xy = {}
q = []
already = [[False for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    a, b = map(int, input().split())
    if i not in xy:
        xy[i] = (a, b)

for _ in range(m):
    a, b = map(int, input().split())
    already[a][b] = True
    already[b][a] = True


for i in range(1, n+1):
    for j in range(i+1, n+1):
        link[i].append(j)
        link[j].append(i)

def calDist(cur, nxt):

    cx, cy = xy[cur]
    nx, ny = xy[nxt]
    d = (cx-nx)**2 + (cy-ny)**2
    return math.sqrt(d)



answer = 0

hp.heappush(q, (0, 1))

while q:
    d, cur = hp.heappop(q)
    
    if len(mst)==n: break

    if not check[cur]:
        check[cur] = True
        
        mst.add(cur)
        if d>0:
            answer+=d

        for nxt in link[cur]:
            if already[cur][nxt]:
                hp.heappush(q, (-1, nxt))
            else:
                nxt_dist = calDist(cur, nxt)
                
                hp.heappush(q, (nxt_dist, nxt))
        

print("{:.2f}".format(answer))
