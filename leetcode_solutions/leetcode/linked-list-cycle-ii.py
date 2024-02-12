# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f=s=head
        flag=False
        while(f and f.next):
            f=f.next.next
            s=s.next
            if(f is s):
                flag=True
                break
        if(not flag):
            return None
        s2=head
        while(s is not s2 ):
            s=s.next
            s2=s2.next
        
        return s