def solution(record):
    answer = []
    enter="님이 들어왔습니다."
    out="님이 나갔습니다."
    
    tmp={}
    
    for val in record:
        if val.split(' ')[0] =="Enter":
            tmp[val.split(' ')[1]]=val.split(' ')[2]
            
            
        elif val.split(' ')[0] == "Change":
             tmp[val.split(' ')[1]]=val.split(' ')[2]
                        
            
   
    for val in record:
        if val.split(' ')[0] == "Enter":
            answer.append(tmp[val.split(' ')[1]]+enter)
            
        elif val.split(' ')[0] == "Leave":
            answer.append(tmp[val.split(' ')[1]]+out)
   
    
    return answer