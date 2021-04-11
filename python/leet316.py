class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        dict = {}
        
        for i in s:
            if i not in dict:
                dict[i] =1
                
            else:
                dict[i]+=1
                
        
        stack =[]
        
        
        for i in range(len(s)):
            
            if s[i] in stack: 
                dict[s[i]]-=1
                continue
                
            if len(stack)==0:
                stack.append(s[i])
                dict[s[i]]-=1
                continue
                
            
            while len(stack) and stack[-1] > s[i] and dict[stack[-1]]>0:
                stack.pop()
             
            
            stack.append(s[i])
            dict[s[i]]-=1
            
            
        
        
        return "".join(stack)
        
        