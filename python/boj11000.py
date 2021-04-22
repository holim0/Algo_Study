import sys, heapq
n = int(input())

arr =[]


for i in range(n):
    s,e = map(int, sys.stdin.readline().split())

    arr.append((s, e))

arr = sorted(arr, key=lambda x: (x[0]))

q = []

heapq.heappush(q, arr[0][1])

for i in range(1,len(arr)):
    if q[0]> arr[i][0]:
        heapq.heappush(q, arr[i][1])
    
    else:
        heapq.heappop(q)
        heapq.heappush(q, arr[i][1])





print(len(q))

