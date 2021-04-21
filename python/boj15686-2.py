import sys
from itertools import combinations


n, m = map(int, input().split())

arr =[]

answer = sys.maxsize

chicken = []

for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)


for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            
            chicken.append((i, j))



johab = list(combinations(chicken, m))

for i in range(len(johab)):
    curjohab = johab[i]
    sum_val=0
    for a in range(n):
        for b in range(n):
            if arr[a][b]==1:
                tmp_dist = sys.maxsize
                for t in curjohab:
                    x, y = t
                    d = abs(x-a)+abs(y-b)
                    
                    tmp_dist = min(tmp_dist, d)

                sum_val+=tmp_dist
    
    answer =min(sum_val, answer)



print(answer)


