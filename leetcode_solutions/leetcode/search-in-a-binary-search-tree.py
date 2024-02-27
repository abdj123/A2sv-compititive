# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if(node):
                if(node.val==val):
                    return node
                l=dfs(node.left)
                r=dfs(node.right)
                if(l):
                    return l
                return r
        k=dfs(root)
        print(k)
        return k