from heapq import *
t = int(input())

while t:

    n, m = map(int, input().split())

    link = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        link[a].append(b)
        link[b].append(a)

    
    answer =-1

    node = []

    h = []

    heappush(h, (1, 1))

    while h:
        cur_w, cur = heappop(h)

        
        if cur not in node:
            node.append(cur)
            answer+=1


            for nxt in link[cur]:
                if nxt not in node:
                    heappush(h, (1, nxt))

    print(answer)




    t-=1