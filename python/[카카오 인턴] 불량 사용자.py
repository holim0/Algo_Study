from itertools import combinations

def solution(user_id, banned_id):
    answer = 1
    
    cur_ban_id = []
    
    real_ban = []
    banned_id.sort()
    
    for ban in banned_id:
        if ban not in real_ban:
            real_ban.append(ban)
    
    def check_same(default, cmp):
        
        if len(default)!=len(cmp): return False
        
        for i in range(len(default)):
            if default[i]!="*":
                if default[i] != cmp[i]: return False
            
        return True
    
    for ban in real_ban:
        for id in user_id:
            if check_same(ban, id):
                if ban not in cur_ban_id:
                    cur_ban_id.append(id)
                    
    def getSol(jobab):
        
        result =[]
        
        
        for cur_johab in johab:
            
            check = [False for _ in range(len(banned_id))]
            tmp =[]
            for j in cur_johab:
                for i in range(len(banned_id)):
                    if check_same(banned_id[i], j) and not check[i] and j not in tmp:
                        check[i]= True
                        tmp.append(j)
            
            if len(tmp)==len(banned_id):
                tmp.sort()
                if tmp not in result:
                    result.append(tmp)
                        
                        
                        
                
        
        print(result)
        
        return len(result)
    
    johab = list(combinations(cur_ban_id, len(banned_id)))

    
    answer = getSol(johab)
    
    
 
                
                
    
    
    
    
    return answer