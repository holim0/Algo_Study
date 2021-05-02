import heapq
import sys
import copy
n = int(input())

max_heap = []

min_heap = []


while n>0:

    number = int(sys.stdin.readline())

    tmp_max = []
    tmp_min= []

    heapq.heappush(max_heap, -number)
    heapq.heappush(min_heap, number)

    

    

    n-=1