n = int(input())
target = int(input())

mapp = [[0 for _ in range(n)] for _ in range(n)]

def check_done(mapp):

    for i in range(n):
        for j in range(n):
            if mapp[i][j]==0:return False
    
    return True

def findIdx(mapp):

    for i in range(n):
        for j in range(n):
            if mapp[i][j]==target:
                return (i+1, j+1)


def getSol(sx, sy, step, number):
    

    if check_done(mapp):
        x, y = findIdx(mapp)
        for i in range(n):
            for j in range(n):
                print(mapp[i][j], end=" ")
            print(end="\n")
        print(x, y)


        exit(0)

    for _ in range(step):
        mapp[sx][sy] = number
        sx+=1
        number-=1
    sx-=1
    sy+=1
    for _ in range(step-1):
        mapp[sx][sy] = number
        sy+=1
        number-=1

    sy-=1
    sx-=1
    for _ in range(step-1):
        mapp[sx][sy] =number
        sx-=1
        number-=1

    sx+=1
    sy-=1
    for _ in range(step-2):
        mapp[sx][sy] = number
        number-=1
        sy-=1
    sy+=1
    sx+=1

   
    
    getSol(sx, sy, step-2, number)





getSol(0, 0, n, n**2)