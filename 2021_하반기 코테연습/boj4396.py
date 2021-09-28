dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]


n= int(input())

bomb = [[0 for _ in range(n)] for _ in range(n)]

def check_range(x,y):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    return False

for i in range(n):
    tmp = input()
    tmp = list(tmp)

    for j in range(len(tmp)):
        if tmp[j]=="*":
            bomb[i][j]=1


isBomb = False
mapp = []

answer = [["." for _ in range(n)] for _ in range(n)]

for i in range(n):
    tmp = input()
    tmp = list(tmp)
    mapp.append(tmp)
    
flag = False
for i in range(n):
    for j in range(n):
        
        if mapp[i][j]=="x" and bomb[i][j]==0:
            cnt=0
            for k in range(8):
                ni, nj = i+dx[k], j+dy[k]
                
                if check_range(ni, nj) and bomb[ni][nj]==1:
                    cnt+=1

            answer[i][j]= str(cnt)
        
        elif mapp[i][j]=="x" and bomb[i][j]==1:
            flag = True
            




if flag:

    for i in range(n):
        for j in range(n):
            if bomb[i][j]==1:
                answer[i][j] = "*"

    
for m in answer:
    print("".join(m))







