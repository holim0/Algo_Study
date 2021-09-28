def reward(cnt):
    
    if 7-cnt>=6:
        return 6
    else:
        return 7-cnt
        


def solution(lottos, win_nums):
    answer = []
    
    lottos.sort()
    win_nums.sort()
    same_cnt = 0
    max_win_cnt = 0
    min_win_cnt = 0
    
    for i in range(6):
        if lottos[i]==0:
            max_win_cnt+=1
        for j in range(6):
            if lottos[i]==win_nums[j]:
                same_cnt+=1
                max_win_cnt+=1
            
            
        
    
    answer = [reward(max_win_cnt),reward(same_cnt)]
    
    
    return answer