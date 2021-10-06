from collections import deque

answer = 1e10

def getSol(f, to, link):
    
    global answer
    
    n = len(link)
    cnt =[]
    q = deque([])
    visit = [False for _ in range(n)]
    
    
 
    for i in range(1, n):
        if not visit[i]:
            visit[i]=True
            tmp = 1
            q.append(i)

            while q:
                cur = q.popleft()

                for k in range(1, n):
                    if not visit[k] and link[cur][k]==1:
                        visit[k]=True
                        tmp+=1
                        q.append(k)

            
            cnt.append(tmp)
    
                        
                
    answer = min(answer, abs(cnt[0]-cnt[1]))    
        
    
    
    
    
    

def solution(n, wires):
    
    global answer
    
    link = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    
    for w in wires:
        f, to = w[0], w[1]
        link[f][to]=1
        link[to][f]=1 
        
    
    for w in wires:
        f, to = w[0], w[1]
        link[f][to], link[to][f]=0, 0
        getSol(f, to, link)
        link[f][to], link[to][f]=1, 1
    
    
    

    
    return answer