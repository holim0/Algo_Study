import heapq
import copy, sys
n, k = map(int, input().split())

jew =  []
bag= []
answer = 0

for i in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(jew, (m, v))




for i in range(k):
    w =int(sys.stdin.readline())
    bag.append(w)


bag.sort()

check= [False for _ in range(n)]

tmp_jew = []
for i in range(len(bag)):
    cur_bag = bag[i]
    
    while True:
        if len(jew)==0: break

        if cur_bag>= jew[0][0]:
            m, v = heapq.heappop(jew)
            heapq.heappush(tmp_jew, -v)

        else: break

    
    if len(tmp_jew)!=0:
        answer+= -heapq.heappop(tmp_jew)
    
    

    

    


print((answer))




