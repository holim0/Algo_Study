import heapq
import sys

input = sys.stdin.readline
n = int(input())


q = []
tmpq = []
for _ in range(n):
    number = int(input())

    if number!=0:
        heapq.heappush(q, (abs(number), number))

    else:
        if len(q)==0:
            print(0)
        else:
            cur = heapq.heappop(q)
            print(cur[1])

        
