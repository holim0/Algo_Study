import sys
input = sys.stdin.readline
n, m = map(int, input().split())

dot = list(map(int, input().split()))

dot.sort()

for _ in range(m):
    start, end  = map(int, input().split())

    l, r = 0, len(dot)-1
    upper, lower = -1, -1
    while l<=r:

        mid = (l+r)//2

        if start>dot[mid]:
            l = mid+1
            
        else:
            upper = mid
            r = mid-1

    l, r = 0, len(dot)-1
    while l<=r:

        mid = (l+r)//2

        if end>=dot[mid]:
            l = mid+1
            lower =mid
        else:
            
            r = mid-1
    if lower-upper<0 or lower==-1 or upper==-1:
        print(0)
    else:
        print(lower-upper+1)