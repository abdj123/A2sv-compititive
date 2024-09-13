# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = set()
        def dfs(node, pth) :
            if not node :
                return 
            dfs(node.right, f'{pth}->{node.val}')
            dfs(node.left, f'{pth}->{node.val}')
            if not (node.right or node.left) :
                res.add(f'{pth}->{node.val}')
        dfs(root, '')
        return [r [2:] for r in list(res)]