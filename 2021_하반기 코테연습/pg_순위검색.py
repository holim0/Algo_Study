from itertools import combinations
def change_lang(cur):
    if cur=="cpp": return "0"
    if cur=="java": return "1"
    if cur=="python": return "2"
    return "o"
def change_job(cur):
    if cur=="backend": return "0"
    if cur=="frontend": return "1"
    return "o"

def change_year(cur):
    if cur=="junior": return "0"
    if cur=="senior": return "1"
    return "o"
    
def change_food(cur):
    if cur=="chicken": return "0"
    if cur=="pizza": return "1"
    return "o"
    



def solution(info, query):
    answer = []
    
    
    dic={}
    idx_g = [0, 1, 2, 3]
    for i in info:
        split_i = i.split(" ")
        personal_info = change_lang(split_i[0]) + change_job(split_i[1]) + change_year(split_i[2]) + change_food(split_i[3])
        
        if personal_info not in dic:
            dic[personal_info] =[int(split_i[-1])]
        else:
            dic[personal_info].append(int(split_i[-1]))
        
        for k in range(1, 5):
            johab = list(combinations(idx_g, k))
            for j in johab:
                tmp_str = list(personal_info)
                
                for alpa in j:
                    tmp_str[alpa]="o"
                
                tmp_str = "".join(tmp_str)
                
                if tmp_str not in dic:
                    dic[tmp_str] = [int(split_i[-1])]
                else:
                    dic[tmp_str].append(int(split_i[-1]))
                    
    for key, val in dic.items():
        dic[key].sort()
    re_q = []
    
    for q in query:
        a = q.split(" and ")
        b = a[-1].split(" ")
        food, target_score = b[0], int(b[1])
        info_q = change_lang(a[0])+change_job(a[1])+ change_year(a[2])+ change_food(food)
        re_q.append((info_q, target_score))
    
    for q in re_q:
        info_q, target_score = q
        
        if info_q not in dic:
            answer.append(0)
            continue
        
        start, end = 0, len(dic[info_q])-1
        
        target_idx = -1
        while start<=end:
            mid = (start+end)//2
            if dic[info_q][mid]>=target_score:
                end = mid-1
                target_idx = mid
            else:
                
                start = mid+1
        
        if target_idx == -1:
            answer.append(0)
            continue
        
        answer.append(len(dic[info_q])-target_idx)
    
    return answer