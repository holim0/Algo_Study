import sys
import heapq
n = int(input())

number =[]

answer = 0

while n>0:

    num = int(sys.stdin.readline())

    heapq.heappush(number, num)
    n-=1



while len(number)>1:

    n1 = heapq.heappop(number)

    n2 = heapq.heappop(number)
    
    answer+=(n1+n2)

    heapq.heappush(number, n1+n2)


print(answer)