import sys

n = int(input())

liquid = list(map(int,(sys.stdin.readline().split())))

dist = sys.maxsize

liquid.sort()


l, r = 0, len(liquid)-1

al, ar = 0, len(liquid)-1

while l<r:
    s = liquid[l]+liquid[r]


    if s==0:
        al, ar =l , r
        break


    if abs(s) < dist:
        al , ar = l, r
        dist = abs(s)

    if s>0:
        r-=1
    elif s<0:
        l+=1

answer =[liquid[ar], liquid[al]]

answer.sort()

print(answer[0], answer[1])
