# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, family, diff):
            family.append(node.val) 
            
            if node.left is not None: 
                diff = dfs(node.left, family, diff)
            if node.right is not None:
                diff = dfs(node.right, family, diff)

            if node.left is None and node.right is None:
                diff = max(diff, max(family) - min(family)) 
            
            family.pop()
            return diff

        return dfs(root, [], 0)