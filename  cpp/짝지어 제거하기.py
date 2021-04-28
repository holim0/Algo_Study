def solution(s):
    answer = 0
    
    list=[]
    for val in s:
        if len(list)>0 and list[-1]==val:
            list.pop()
            continue
        list.append(val)
        
        
    
    if len(list)==0:
        answer=1
    return answer