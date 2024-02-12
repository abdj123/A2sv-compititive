# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        count_a=0
        count_b=0
        itr1=headA
        itr2=headB
        while(itr1):
            count_a+=1
            itr1=itr1.next
        while(itr2):
            count_b+=1
            itr2=itr2.next
        itr1=headA
        itr2=headB

        if count_a > count_b:
            for i in range(count_a-count_b):
                itr1=itr1.next
        elif count_b > count_a:
            for i in range(count_b-count_a):
                itr2=itr2.next

        while itr1 and itr2 and itr1 != itr2:
            itr1 = itr1.next
            itr2 = itr2.next
            
        if itr1 is itr2:
            return itr1
        
        return None
