mapp =[]

answer = 1e10

for _ in range(10):
    tmp =list(map(int, input().split()))
    mapp.append(tmp)

loc = []

check = [[False for _ in range(10)] for _ in range(10)]
paper = [0, 5, 5, 5, 5, 5]

for i in range(10):
    for j in range(10):
        if mapp[i][j]==1:
            loc.append((i,j))

def patch(x, y, size):
    for i in range(x, x+size):
        for j in range(y, y+size):
            check[i][j] = True

def detach(x, y, size):
    for i in range(x, x+size):
        for j in range(y, y+size):
            check[i][j] = False




def isOk(x, y, size):

    if x+size>10 or y+size>10: return False

    for i in range(x, x+size):
        for j in range(y, y+size):
            if mapp[i][j]!=1 or check[i][j]==True:
                return False
    return True


def getSol(curIdx, cnt):
    global answer
    

    if curIdx==len(loc):
        answer=min(answer, cnt)
        return 

    cx, cy = loc[curIdx]
    if check[cx][cy]:
        getSol(curIdx+1, cnt)
    
    for s in range(1, 6):
        if isOk(cx, cy, s) and paper[s]>0:
            patch(cx, cy, s)
            paper[s]-=1
            getSol(curIdx+1, cnt+1)
            detach(cx, cy, s)
            paper[s]+=1
            

    
    
getSol(0, 0)

if answer == 1e10:
    print(-1)

else:
    print(answer)