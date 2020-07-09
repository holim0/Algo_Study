import collections


def solution(clothes):
    answer = 1
    
    kind=[];
    
    for i, j in clothes:
        kind.append(j)
        

    kind = collections.Counter(kind)
    
    for i in kind.values():
        answer *= (i+1)
    
        
      
    answer-=1
       

    return answer