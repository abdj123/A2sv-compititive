# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        li=[]
        node=head
        while node:
            li.append(node.val)
            node=node.next
        while left<right:
            li[left-1],li[right-1]=li[right-1],li[left-1]
            left+=1
            right-=1
        Node=head
        i=0
        while Node:
            Node.val=li[i]
            Node=Node.next
            i+=1
        return head
