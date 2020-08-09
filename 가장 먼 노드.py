from collections import Counter as c
from collections import deque

def solution(n, edge):
    answer = 0
    
    adjlist=[[] for _ in range(n + 1)]
    
    check=[False for i in range(n+1)]
    
    
    
    for x, y in edge:
        adjlist[x].append(y)
        adjlist[y].append(x)
        
    
    q=deque()
    q.append(1)
    check[1]=True;
    
    visit= [0 for i in range(n+1)]
    
    maxval=-1
    while q:
        base =q.popleft()
        for i in adjlist[base]:
            if check[i]==False :
                check[i]=True
                q.append(i)
                visit[i]+=visit[base]+1
                if maxval < visit[i]:
                    maxval=visit[i]
                
        
    
    
    
    for val in visit:
        if maxval==val:
            answer+=1
    

    return answer