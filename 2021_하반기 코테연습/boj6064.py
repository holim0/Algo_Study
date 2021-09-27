import sys

input = sys.stdin.readline


T = int(input())

while T:

    M, N, x, y = map(int, input().split())

    
    answer = -1
    sx, sy = 1, 1
    day = 1
    while True:

        
        if sx<M:
            sx+=1

        else:
            sx=1

        if sy<N:
            sy+=1
        else:
            sy=1

        if sx==x and sy==y:
            answer = day+1
            break

        if sx==M and sy==N:
            break

        day+=1

    print(answer)





    T-=1