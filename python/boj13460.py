import sys

sys.setrecursionlimit(10**4)

n, m = map(int, input().split())

dir = {
    "U" : [-1, 0],
    "D" : [1, 0],
    "L" : [0, -1],
    "R" : [0, 1]
}

not_go = {
    "U" : "D",
    "D" : "U",
    "R": "L",
    "L" : "R"
}

board = []
answer = sys.maxsize


for i in range(n):
    s = list(input())
    board.append(s)

rx, ry, bx, by =0, 0, 0, 0

tx, ty = 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j]=="R":
            rx, ry = i, j
        elif board[i][j]=="B":
            bx, by = i, j

        elif board[i][j] =="O":
            tx, ty = i, j



def getSol(curDir, curRx, curRy, curBx, curBy, cnt):
    
    if cnt>10:
        return 
    global answer
    oriRx, oriRy, oriBx, oriBy = curRx, curRy, curBx, curBy
    
    isRedIn, isBlueIn = False, False
    while True:
        nextRx, nextRy = curRx+dir[curDir][0], curRy+dir[curDir][1]
        
        if board[nextRx][nextRy]=="O":
            isRedIn =True
            break

        if board[nextRx][nextRy]== "#":
            break
    
        curRx, curRy = nextRx, nextRy
            

    while True:
        nextBx, nextBy = curBx+dir[curDir][0], curBy+dir[curDir][1]
        
        if board[nextBx][nextBy]=="O":
            isBlueIn = True
            break
            
        if board[nextBx][nextBy]== "#":
            break
    
    
        curBx, curBy = nextBx, nextBy
    
    
    
    
    
    


    if isBlueIn : return 
    else:
        if isRedIn:
            answer= min(answer, cnt+1)
            return

    

    if curRx==curBx and curRy == curBy:
        if curDir =="U":
            if oriRx < oriBx:
                curBx +=1
            else:
                curRx+=1  
        elif curDir =="D":
            if oriRx < oriBx:
                curRx-=1
            else:
                curBx-=1
        elif curDir=="R":
            if oriRy < oriBy:
                curRy-=1
            else:
                curBy-=1
        elif curDir =="L":
            if oriRy < oriBy:
                curBy+=1
            else:
                curRy+=1

    

    if curDir =="U" or curDir=="D":
        getSol("L", curRx, curRy, curBx, curBy, cnt+1)
        getSol("R", curRx, curRy, curBx, curBy, cnt+1)
    else:
        getSol("U", curRx, curRy, curBx, curBy, cnt+1)
        getSol("D", curRx, curRy, curBx, curBy, cnt+1)


if __name__ == "__main__":
    for key in dir.keys():
        getSol(key, rx, ry, bx, by, 0)


if answer > 10 :
    print(-1)

else:
    print(answer)