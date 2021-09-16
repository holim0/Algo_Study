def get_ratio(s,number, w):
    
    size= len(s)
    w_cnt = 0
    l_cnt = 0
    h = 0
    
    for i in range(len(s)):
        if s[i]=="N": size-=1
            
        elif s[i]=="W": 
            w_cnt+=1
            
            if w[number]< w[i]: h+=1
            
    
    if size==0: return 0, h
    
    return w_cnt/size, h
        


def solution(weights, head2head):
    answer = []
    
    info = []
    
    
    for i in range(len(weights)):
        cur = weights[i]
        
        win_ratio, heavy_cnt = get_ratio(head2head[i], i, weights)
        
        info.append((win_ratio, heavy_cnt, cur, i))
        
        
    sorted_info = sorted(info, key= lambda x : (-x[0], -x[1], -x[2], x[3]))
    
    for i in range(len(sorted_info)):
        n = sorted_info[i][3]
        answer.append(n+1)
        
    
    
    return answer