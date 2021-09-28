from collections import defaultdict

def solution(enter, leave):
    answer = [0 for _ in range(len(enter))]
    
    out = 0
    enter_q = []
    dict = defaultdict(int)
    
    for i in range(len(enter)):
        in_cur = enter[i]
        
        enter_size = len(enter_q)
        answer[in_cur-1]+=enter_size
        
        for j in enter_q:
            answer[j-1]+=1
        
        enter_q.append(in_cur)
        
        
        while True:
            if out>=len(leave): break
            
            if leave[out] not in enter_q: break
            else:
                enter_q.remove(leave[out])
                out+=1
        
    
    
    
    

        
    
    
        
            
            
        
        
        
    
    
    
    
    return answer