from itertools import combinations_with_replacement


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer=[]
        
        def dfs(sum_val, idx, path):
            
            if sum_val>target:
                return
            
            if sum_val==target:
                answer.append(path)
                return
            
            
            
            for i in range(idx, len(candidates)):
                new_path = path+ [candidates[i]]
                dfs(sum_val+candidates[i], i, new_path)
        
        
        
        for i in range(len(candidates)):
            dfs(candidates[i], i, [candidates[i]])
            
        
        
        return answer