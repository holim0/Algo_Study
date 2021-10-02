def solution(n, s, a, b, fares):
    answer = 1e10
    INF = 1e10
    link = [[INF for _ in range(n+1)] for _ in range(n+1)]
    
    
    for f in fares:
        start, to, c = f
        link[start][to] = c
        link[to][start] = c
     
    for i in range(1, n+1):
        link[i][i]=0
        
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if link[i][j]>link[i][k]+link[k][j]:
                    link[i][j] = link[i][k]+link[k][j]
                
    
    for i in range(n+1):
        sum = link[s][i]+link[i][a]+link[i][b]
        if answer > sum:
            answer = sum
        
    
    
    
    
    return answer