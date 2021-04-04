from itertools import combinations



def compare(s1, s2):
    
    for v in s1:
        if v not in s2:
            return False
        
    return True
    

def solution(orders, course):
    answer = []
    
    cnt_dict = {}
    
    for o in orders:
        o = list(o)
        o.sort()
        johab = []
        for c in course:
            tmp = list(combinations(o, c))
            johab += tmp
        
        
        for j in johab:
            j = list(j)
            j.sort()
            j = "".join(j)
            if j not in cnt_dict:
                cnt_dict[j] =1
            else:
                cnt_dict[j]+=1
                
    max_dict={}
        
    for key, value in cnt_dict.items():
        if value >=2:
            if len(key) not in max_dict:
                max_dict[len(key)] = value
                
            else:
                max_dict[len(key)] = max(value, max_dict[len(key)])

                
    for key, value in cnt_dict.items():
        if value>=2:
            if value == max_dict[len(key)]:
                answer.append(key)


    answer.sort()
    
    
    return answer