import heapq
import sys

n = int(input())

q = []

for i in range(n):
    num = int(sys.stdin.readline())

    if num==0:
        if len(q)==0:
            print(0)
        else:
            print(heapq.heappop(q))


    else:
        heapq.heappush(q, num)
    