def solution(weight):
    answer = 0
    weight.sort()
    
    base=weight[0]
    
    for i in range(1, len(weight)):
        if base+1< weight[i]:
            break
        else:
            base+=weight[i]
        
    
    
    
    return base+1