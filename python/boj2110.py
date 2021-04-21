import sys

n, c =map(int,input().split())

arr = []

for i in range(n):
    x = int(sys.stdin.readline())

    arr.append(x)

arr.sort()

l, r = 1, arr[-1]-arr[0]

answer =0
while l<=r:

    mid= (l+r)//2

    start= arr[0]
    cnt = 1
    for i in range(1, len(arr)):
        dist = arr[i]-start

        if mid<=dist:
            cnt+=1
            start = arr[i]
        
    #  print(l, r,mid, cnt)
    
    if cnt>=c:
        l= mid+1
        answer= mid;
    else:
        r = mid-1

    
print(answer)
    
