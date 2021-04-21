import sys
n = int(input())

arr = list(map(int, sys.stdin.readline().split()))


dp = [1 for _ in range(len(arr))]

for i in range(1, len(arr)):

    if i==1:
        if arr[i]>arr[i-1]:
            dp[i]=2
        continue

    cur = arr[i]
    l, r = 0, i-1


    while l<=r:

        mid = (l+r)//2

        if mid<cur:
            dp[i]= max(dp[i], dp[mid])

        
