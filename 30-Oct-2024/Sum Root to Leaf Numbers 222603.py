# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, prev):
            val = str(node.val)
            if not node.left and not node.right:
                self.sum += int(prev + val)
            if node.left:
                dfs(node.left, prev + val)
            if node.right:
                dfs(node.right, prev + val)
        
        self.sum = 0
        dfs(root, '')
        return self.sum