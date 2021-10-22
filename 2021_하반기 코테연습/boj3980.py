

c = int(input())

abil = []
check = [False for _ in range(11)]
answer = 0
def find(cur, cnt):
    global answer, abil, check
    if cur==11:
        answer = max(answer, cnt)        


    for i in range(11):
        if not check[i] and abil[cur][i]!=0:
            check[i]= True
            find(cur+1, cnt+abil[cur][i])
            check[i] = False
    

while c:


    abil = []
    answer = 0
    check = [False for _ in range(11)]

    for _ in range(11):
        tmp = list(map(int, input().split()))
        abil.append(tmp)

    
    find(0, 0)
    
    print(answer)

    





    c-=1