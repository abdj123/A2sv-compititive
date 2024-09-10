# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = head

        while itr.next:
            temp = itr.next
            num = gcd(itr.val, itr.next.val)
            node = ListNode(val=num, next=itr.next)
            itr.next = node
            itr = temp
        return head
