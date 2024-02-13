# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        f=s=head
        count=0
        if(not head):
            return head
        
        while(f):
            count+=1
            f=f.next
        f=head            
        k=k%count
        
        if(not head.next or k==0):
            return head
        
        for i in range(k):
            f=f.next
        
        while(f.next):
            f=f.next
            s=s.next
        
        temp=s.next
        f.next=head
        head=temp
        s.next=None
        
        return head
        
        