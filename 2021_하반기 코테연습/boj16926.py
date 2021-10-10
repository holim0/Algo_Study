n,m, r= map(int, input().split())

mapp = []


for _ in range(n):
    tmp = list(map(int, input().split()))
    mapp.append(tmp)

def printmapp():

    for i in range(n):
        for j in range(m):
            print(mapp[i][j], end=" ")
        print(end="\n")

    

def spin(x, y, sizen, sizem):

    if x>=n or y>=m or sizen<=0 or sizem<=0:
        
        return  
    
    curn, curm = x+sizen, y+sizem


    tmp1 = mapp[curn-1][y]
    # print(x, y,sizen, sizem)

    for i in range(curn-1, x, -1):
        mapp[i][y] = mapp[i-1][y]

    tmp2 = mapp[curn-1][curm-1]

    for i in range(curm-1, y+1, -1):
        mapp[curn-1][i] = mapp[curn-1][i-1]
    
    mapp[curn-1][y+1] = tmp1

    tmp3 = mapp[x][curm-1]

    for i in range(x, curn-2):
        mapp[i][curm-1] = mapp[i+1][curm-1]
    mapp[curn-2][curm-1] = tmp2

    for i in range(y, curm-2):
        mapp[x][i] = mapp[x][i+1]
    mapp[x][curm-2] = tmp3

    # printmapp()

    
    spin(x+1, y+1, sizen-2, sizem-2)








for _ in range(r):
    spin(0, 0, n, m)

printmapp()