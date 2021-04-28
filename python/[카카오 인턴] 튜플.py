import re
def solution(s):
    answer = []
    
    s = s[1:len(s)-1]
    
    s= s.split("}")
    
    sorted_s = sorted(s, key = lambda x : len(x))

    for cur_s in sorted_s:
        cur_s = re.split("[ , | { | }]", cur_s)
       
        for s in cur_s:
            if s.isdigit():
                if int(s) not in answer:
                    answer.append(int(s))
        
                    
    
   
    

    
    
    return answer