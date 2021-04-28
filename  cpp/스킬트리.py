def solution(skill, skill_trees):
    answer = 0
    
    
    for s in skill_trees:
        tmp=""
        for alpa in s:
            if alpa in skill:
                tmp+=alpa
        
       
        if len(tmp)==len(skill):
            if tmp==skill:
                answer+=1
        else:
            flag=False 
            for i in range(len(tmp)):
                if tmp[i] != skill[i]:
                    flag=True
                    break
            
            if flag==False:
                answer+=1
    return answer