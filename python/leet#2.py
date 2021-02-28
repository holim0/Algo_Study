# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        a = ""
        b = ""
        cur = l1
        while True:
            val = cur.val
            a += str(val)

            cur = cur.next
            if cur == None:
                break

        cur = l2
        while True:
            val = cur.val
            b += str(val)

            cur = cur.next
            if cur == None:
                break

        a = a[::-1]
        b = b[::-1]

        sum_val = int(a) + int(b)

        sum_val = str(sum_val)

        sum_val = list(sum_val[::-1])

        answer = ListNode(int(sum_val[0]))
        cur = answer
        for i in range(1, len(sum_val)):
            next = ListNode(int(sum_val[i]))

            cur.next = next
            cur = cur.next

        return answer
