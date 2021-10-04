class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1_p = 0
        n2_p = 0
                
        answer = []
        
        
        while n1_p<len(nums1) and n2_p<len(nums2):
            
            if len(nums1)-n<=n1_p<len(nums1) and nums1[n1_p]==0:
                n1_p+=1
                
            else:
                
                if nums1[n1_p]>nums2[n2_p]:
                    answer.append(nums2[n2_p])
                    n2_p+=1
                    
                else:
                    answer.append(nums1[n1_p])
                    n1_p+=1
        
        
        
        if n2_p<len(nums2):
            for i in range(n2_p, len(nums2)):
                answer.append(nums2[i])
            
            
        elif n1_p<len(nums1):
            for i in range(n1_p, len(nums1)):
                if i>=len(nums1)-n and nums1[i]==0: continue
                answer.append(nums1[i])
                    
        
        nums1[:] = answer[:]
        
        