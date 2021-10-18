n = int(input())

switch = list(map(int,input().split()))
switch.insert(0, 0)
m = int(input())



def change(x):
    if x==1: return 0
    elif x==0: return 1




for _ in range(m):
    a, b = map(int, input().split())

    ## 남자
    if a==1:
        idx = b

        while idx<=n:
            switch[idx] = change(switch[idx])
            idx+=b
    
    ## 여자
    elif a==2:
        l, r = b-1, b+1

        if b-1>0 and b+1<=n:
            while l>0 and r<=n:
                if switch[l]!=switch[r]:break
                    
                else:
                    switch[l] = change(switch[l])
                    switch[r] = change(switch[r])
                    l-=1
                    r+=1
        

        switch[b] = change(switch[b])

for i in range(1, len(switch)):
    print(switch[i], end=" ")
    
    if i>0 and i%20==0:
        print("")