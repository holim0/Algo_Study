n, c = map(int, input().split())

home = []


for _ in range(n):
    tmp = int(input())
    home.append(tmp)
answer =-1

home.sort()

l, r = 1, home[-1] - home[0]


while l<=r:
    
    mid = (l+r)//2


    cnt = 1

    cur = home[0]
    for i in range(1, len(home)):
        if home[i]-cur>=mid:
            cnt+=1
            cur = home[i]

    
    if cnt<c:
        r = mid-1
    else:
        
        answer = max(mid, answer)
        l = mid+1

print(answer)       
    