import copy

mapp =[]

empty = []

for _ in range(9):
    tmp = list(map(int, input().split()))
    mapp.append(tmp)


for i in range(9):
    for j in range(9):
        if mapp[i][j]==0:
            empty.append((i, j))

def getArea(i, j):
    if 0<=i<3:
        if j<=2:
            return (0, 0)
        if j<=5:
            return (0, 3)
        if j<=8:
            return (0, 6)
    if 3<=i<6:
        if j<=2:
            return (3, 0)
        if j<=5:
            return (3, 3)
        if j<=8:
            return (3, 6)
    if i>=6:
        if j<=2:
            return (6, 0)
        if j<=5:
            return (6, 3)
        if j<=8:
            return (6, 6)




def getAV(i, j, cur_mapp):
    av = []
    check = [False for _ in range(10)]
    ## 가로 체크
    for row in range(9):
        cur = cur_mapp[i][row]
        check[cur] = True
    ## 세로 체크
    for col in range(9):
        cur = cur_mapp[col][j]
        check[cur]=True
    
    ## 영역 체크

    sx, sy = getArea(i, j)

    for i in range(sx, sx+3):
        for j in range(sy, sy+3):
            cur = cur_mapp[i][j]
            check[cur] = True

    
    for i in range(1, 10):
        if not check[i]:
            av.append(i)

    return av




def getSol(cnt):


    if cnt==len(empty):
        for i in range(9):
            for j in range(9):
                print(mapp[i][j], end=" ")
            print(end="\n")
        exit(0)
    

    
        
    
    empty_i, empty_j = empty[cnt]

    av = getAV(empty_i, empty_j, mapp)
    
    for a in av:
        mapp[empty_i][empty_j] = a
        getSol(cnt+1)
        mapp[empty_i][empty_j] = 0
            
                

            
            
                
                
getSol(0)