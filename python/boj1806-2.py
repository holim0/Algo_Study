import sys
n, S = map(int, input().split())


arr = list(map(int, input().split()))

acc= [arr[0]]

for i in range(1, len(arr)):
    acc.append(acc[-1]+arr[i])


s, e = 0, 0

min_len = sys.maxsize

while s<len(acc) and e<len(acc):

    sum_val = 0


    if s == 0:
        sum_val= acc[e]

    else:
        sum_val =acc[e]-acc[s-1]

    
    if sum_val>=S:
        min_len = min(min_len, e-s+1)
        s+=1

    else:
        e+=1

if min_len==sys.maxsize:
    print(0)
else:
    print(min_len)