from itertools import combinations
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits =="":
            return []

        number_map ={
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7:  ["p", "q", "r", "s"],
            8:  ["t", "u", "v"],
            9:  ["w", "x", "y", "z"]
        }
        
        tmp =[]
        for i in range(len(digits)):
            cur = int(digits[i])
            print(cur)
            if int(digits[i]) in number_map:
                tmp.append(number_map[cur])
                
        
        
        answer= list(product(*tmp))
        result = []
        for i in range(len(answer)):
            cur = "".join(list(answer[i]))
            result.append(cur)
        
        return result
        