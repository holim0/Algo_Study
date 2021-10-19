import sys
# sys.setrecursionlimit(10*6)
k = int(input())

number = list(map(int, input().split()))

answer = [[] for _ in range(k)]




def getSol(cur, dep):
    
    if len(cur)==0: return 
    size = len(cur)

    mid = size//2
    
    answer[dep].append(cur[mid])


    getSol(cur[:mid], dep+1)
    getSol(cur[mid+1:], dep+1)

getSol(number, 0)

for i in range(k):
    for j in range(len(answer[i])):
        print(answer[i][j], end=" ")
    print("")