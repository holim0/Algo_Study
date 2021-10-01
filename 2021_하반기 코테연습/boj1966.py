import heapq
from collections import deque

t = int(input())


while t:


    n, m = map(int, input().split())


    number = list(map(int, input().split()))

    h = []
    q = deque([])

    for i in range(len(number)):
        q.append((number[i], i))
        heapq.heappush(h, (-number[i]))

    cnt = 0 
    while q:

        cur, idx = q.popleft()
        max_cur= heapq.heappop(h)
        
        if -max_cur > cur:
            q.append((cur, idx))
            heapq.heappush(h, max_cur)

        else:
            cnt+=1
            if idx == m:
                print(cnt)
                break
            

        





    t-=1
