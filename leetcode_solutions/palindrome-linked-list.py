# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp=[]
        itr=head
        while(itr):
            temp.append(itr.val)
            itr=itr.next
        if(temp[:]==temp[::-1]):
            return True
        else:
            return False