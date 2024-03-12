# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res=[]
        def bst(node):
            if(not node):
                return
            if(node.val>=low and node.val<=high):
                res.append(node.val)
            bst(node.left)
            bst(node.right)
        bst(root)
        return sum(res)
