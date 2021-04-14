# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        answer =[]
       
        for i in range(len(lists)):
            cur = lists[i]
            
            while True:
                
                if cur==None:
                    break
                answer.append(cur.val)
                cur = cur.next
        
        if len(answer)==0:
            return
        answer.sort()
        
        cur = ListNode(answer[0])
        output = cur
        for i in range(len(answer)):
            
            if i==len(answer)-1:
                output.next=None
                break
            
            output.next = ListNode(answer[i+1])
            output = output.next
            
         
        
           
            
        return cur  
        
        
            