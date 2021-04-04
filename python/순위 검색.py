from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    answer = []
    
    
    
    
    
    indexing = {}
    
    
    for i in info:
        tmp_value = ""
        
        to_list = i.split()
        
        for i in range(len(to_list)-1):
            tmp_value+= to_list[i]
            
        idx_list =[0, 1, 2, 3]
        
        for i in range(0, 5):
            johab = list(combinations(idx_list, i))
            for j in johab:
                
                tmp = ""
                for k in range(4):
                    if k not in j:
                        tmp+=to_list[k]
                    else:
                        tmp+="-"
                
                if tmp not in indexing:
                    indexing[tmp] = [int(to_list[-1])]
                else:
                    indexing[tmp].append(int(to_list[-1]))
            
        
    for key in indexing.keys():
        indexing[key].sort()
       
        
        
   
    
    for q in query:
        
        list_q = q.split(" ")
        index= list_q[0] + list_q[2] + list_q[4] + list_q[6]
        score = int(list_q[7])
        
        
        if index not in indexing.keys(): 
            answer.append(0)
        
        else:
            s, e = 0, len(indexing[index])
            while s<e:
                mid =(s+e)//2
                if indexing[index][mid] < score:
                    s= mid+1

                elif indexing[index][mid] >=score:
                    e = mid
            
            answer.append(len(indexing[index])-e)
            
        
        
    
    
        
    
    
    
    return answer