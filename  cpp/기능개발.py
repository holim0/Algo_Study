def solution(progresses, speeds):
    answer = []
    m=[]
    day=[]
    
    for a, b in zip(progresses, speeds):
        m.append([a, b])
        
    for v1, v2 in m:
        tmp=(100-v1)//v2
        tmp2=(100-v1)%v2
        
        if tmp2!=0 :
            day.append(tmp+1)
        else:
            day.append(tmp)
            
    start=0    
    while True :   
        cnt=1
        if start==len(day)-1:
            answer.append(cnt)
            return answer
        for sec in range(start+1, len(day)):
            if day[start]>=day[sec]:
                cnt+=1
                if sec==len(day)-1:
                    answer.append(cnt)
                    return answer
                    
            else:
                answer.append(cnt)
                start=sec
                break
                
        
    return answer