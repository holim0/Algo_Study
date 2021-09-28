from collections import defaultdict
def solution(nums):
    answer = 0
    
    monster = defaultdict(int)
    
    for n in nums:
        monster[n]+=1
        
    monster_kind = len(monster)

    if len(nums)//2 <= monster_kind:
        return len(nums)//2
    
    else:
        return monster_kind