# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        is_p_null = p is None
        is_q_null = q is None
        
        if is_p_null and is_q_null:
            return True
        elif is_p_null or is_q_null:
            return False
        else:
            status = p.val == q.val
            status = status and self.isSameTree(p.left, q.left)
            status = status and self.isSameTree(p.right, q.right)
            return status
        