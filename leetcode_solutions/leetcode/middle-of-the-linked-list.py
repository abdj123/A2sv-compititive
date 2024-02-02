# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr=head
        count=count1=0
        while(itr):
            itr=itr.next
            count+=1
        itr=head
        mid=count//2
        if(count==1): return itr
        while(itr):
            itr=itr.next
            count1+=1
            if(count1==mid):
                break
        return itr


            


