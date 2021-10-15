import heapq as hp
import sys
input = sys.stdin.readline

n, m = map(int, input().split())


link = [[] for _ in range(n+1)]



for _ in range(m):
    a, b, c = map(int, input().split())
    link[a].append((b, c))
    link[b].append((a, c))

q = []
hp.heappush(q, (0, 1))

mst = 0
check = [False for _ in range(n+1)]
cost_arr = []
answer = 0
max_val = -1

while q:
    cur_cost, cur = hp.heappop(q)
    
    if mst==n: break

    if not check[cur]:
        check[cur]=True
        mst+=1
        max_val = max(max_val, cur_cost)
        answer+=cur_cost

    for nxt in link[cur]:
        nn, n_cost = nxt
        if not check[nn]:
            hp.heappush(q, (n_cost, nn))


print(answer-max_val)