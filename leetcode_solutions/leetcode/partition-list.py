# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        below_dummy=ListNode(None)
        above_dummy=ListNode(None)
        above,below=above_dummy,below_dummy
        
        itr=head
        above_head=above_dummy
        
        if(not head or not head.next):
            return head
        
        while(itr):
            if(itr.val<x):
                below.next=itr
                below=below.next
            else:
                above.next=itr
                above=above.next
            itr=itr.next
        
        print(above_head)

        above.next=None
        below.next = above_head.next
        head=below_dummy.next
        return head