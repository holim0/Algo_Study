n, m = map(int, input().split())


check = [0 for _ in range(n+1)]
nothing = 0
dict = {}

for _ in range(m):
    tmp = input()
    tmp = tmp.split(" ")
    a = int(tmp[0])
    i = int(tmp[1])
    
    x = -1
    
    if len(tmp)>2:
        x = int(tmp[2])
    

    if a==1:
        train = check[i]

        target = 1<<(x-1)
        
        check[i] = train | target

    elif a==2:
        check[i] = check[i] & ~(1<<(x-1))
        
    elif a==3:
        check[i] = check[i]<<1
        check[i] &= ~(1<<20)
       
    elif a==4:
        check[i] = check[i]>>1
        
        
       


answer =0

for i in range(1, n+1):

    if check[i] not in dict:
        dict[check[i]] = True
        answer+=1

print(answer)    