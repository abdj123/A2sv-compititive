# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if(node):
                res.append(node.val)
                node.left=dfs(node.left)
                node.right=dfs(node.right)
        res=[]
        dfs(root)
        count=Counter(res)
        max_=max(count.values())
        res=[]
        for k,v in count.items():
            if(v==max_):
                res.append(k)
        return res