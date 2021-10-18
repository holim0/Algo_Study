n = int(input())

number = list(map(int, input().split()))

m = int(input())

l, r = 1, max(number)

answer = -1

while l<=r:

    mid = (l+r)//2
    
    cur_s = 0

    for n in number:
        if n>=mid:
            cur_s+=mid
        else:
            cur_s+=n

    
    if cur_s>m:
        r = mid-1

    else:
        answer = mid
        l = mid+1

print(answer)