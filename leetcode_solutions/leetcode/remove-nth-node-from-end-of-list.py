# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(not head or not head.next):
            return None
        itr=head
        k=0
        
        while(itr):
            k+=1
            itr=itr.next
        itr=head
        rng=k-n
        
        if(rng==0):
            head=head.next
            return head
        
        for i in range(rng-1):
            itr=itr.next
        itr.next=itr.next.next

        return head
        