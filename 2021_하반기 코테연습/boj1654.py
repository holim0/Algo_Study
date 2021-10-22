k, n = map(int, input().split())

number = []

for _ in range(k):
    tmp = int(input())
    number.append(tmp)

l, r = 1, max(number)

answer = 0


while l<=r:

    cnt = 0
    mid = (l+r)//2
    
    for nn in number:
        if nn>=mid:
            cnt+=nn//mid
    
    if cnt<n:
        r = mid-1
    else:
        answer = mid
        
        l = mid+1


print(answer)