# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=[]
        while(head):
            temp.append(head.val)
            head=head.next
        output=sorted(temp)

        dummy=itr=ListNode()

        for i in output:
            itr.next=ListNode(i)
            itr=itr.next
        return dummy.next




