import sys

k, n = map(int, input().split())

arr = []

for i in range(k):
    tmp = int(sys.stdin.readline())
    arr.append(tmp)

arr.sort()

l, r = 1, arr[-1]

answer = 0

while l<=r:

    mid = (l+r)//2


    cnt = 0

    for i in range(len(arr)):
        cnt+= arr[i]//mid
    

    if cnt<n:
        r = mid-1
        
    else:
        l= mid+1
        answer = mid
        
        

print(answer)