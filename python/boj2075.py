import heapq

n = int(input())

arr =[]
q = []
for i in range(n):

    tmp = list(map(int, input().split()))
    arr.append(tmp)



for i in range(n):
    for j in range(n):

        heapq.heappush(q, arr[i][j])
        if len(q)>n:
            heapq.heappop(q)

        

        

cnt = 0

answer= heapq.heappop(q)


print(answer)