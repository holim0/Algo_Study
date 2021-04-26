n = int(input())

money = list(map(int, input().split()))

m = int(input())

l, r = 1, max(money)
answer=0
while l<=r:

    mid =(l+r)//2

    sum_val =0

    for i in range(len(money)):
        if money[i]>mid:
            sum_val+=mid
        else:
            sum_val+=money[i]
    
    
    if sum_val>m:
        r= mid-1

    else:
        answer=mid
        l= mid+1

print(answer)

