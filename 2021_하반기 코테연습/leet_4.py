class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        p1, p2 = 0, 0
        
        
        merged = []
        
        
        while p1<len(nums1) and p2<len(nums2):
            
            
            if nums1[p1]>nums2[p2]:
                merged.append(nums2[p2])
                p2+=1
                
            else:
                merged.append(nums1[p1])
                p1+=1

                
        
        if p1<len(nums1):
            
            while p1<len(nums1):
                merged.append(nums1[p1])
                p1+=1
        
        
        
        if p2<len(nums2):
            while p2<len(nums2):
                merged.append(nums2[p2])
                p2+=1
                
        answer = float(0)    
        if len(merged)%2 ==0:
            base = len(merged)//2
            
            answer= (merged[base-1]+merged[base])/2
            
        else:
            base = len(merged)//2
            
            answer= merged[base]
            
        
        return answer
            