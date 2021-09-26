import heapq
import sys

input = sys.stdin.readline

r, c, n = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

mapp = []
for _ in range(r):
    tmp =input()
    tmp = tmp.rstrip()
    mapp.append(list(tmp))

time = 0



bomb = [[-1 for _ in range(c)] for _ in range(r)]

for i in range(r):
    for j in range(c):       
        if mapp[i][j]=="O":
            bomb[i][j] = 0
            




time+=1

dx=[1, -1, 0, 0]
dy= [0, 0, -1, 1]

def check_range(x,y):

    if x>=0 and x<r and y>=0 and y<c:
        return True
    return False

while True:

    if time==n:
        break
    time+=1

    flag = False

    for i in range(r):
        for j in range(c):
            if bomb[i][j] == -1:
                flag = True
                break
    
    if flag:
        for i in range(r):
            for j in range(c):
                if bomb[i][j]==-1:
                    bomb[i][j] = time
    
    else:
        for i in range(r):
            for j in range(c):
                if time-bomb[i][j]==3:
                    bomb[i][j] = -1
                    
                    for k in range(4):
                        nr, nc = i+dx[k], j+dy[k]
                        
                        if check_range(nr, nc) and time-bomb[nr][nc]!=3:
                    
                            bomb[nr][nc] =-1

    
    

answer= []

for i in range(r):
    tmp=""
    for j in range(c):
        if bomb[i][j]!=-1:
            tmp+="O"
        else:
            tmp+="."

    answer.append(tmp)


for i in range(r):
    print(answer[i])

    
    


    



    