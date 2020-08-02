result=987654321

def dfs(cnt, num, n, target):
    
    if cnt>8:
        return
    if num==target:
        global result
        result=min(result, cnt)
        
    val=0
    
    for i in range(0, 8):
        val=val*10+n
        
        dfs(cnt+i+1, num+val, n, target)
        dfs(cnt+i+1, num-val, n, target)
        
        if num!=0:
            dfs(cnt+i+1, num*val, n, target)
            dfs(cnt+i+1, num/val, n, target)
            
        
    


def solution(N, number):
    
    
    answer = 0
    
    dfs(0, 0, N,number)
    
    if result==987654321:
        return -1
    
    answer=result
    return answer