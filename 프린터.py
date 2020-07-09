def solution(priorities, location):
    answer = 0
    
    tmp=[]
    
    
    dict=[]
    for i in range(len(priorities)):
        dict.append([i, priorities[i]])
        
    
    
    while len(dict)!=0:
        first=dict[0][1]
        
        check=False
        for i in range(1, len(dict)):
            if(first<dict[i][1]):
                check=True
                dict.append([dict[0][0], first])
                dict.pop(0)
                break
        if check==False:
            tmp.append([dict[0][0],first])
            dict.pop(0)
        
    
    
    for i in range(len(tmp)):
        if(tmp[i][0]==location):
            answer=i+1
            break
        
    
    
    return answer