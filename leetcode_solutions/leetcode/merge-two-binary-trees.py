# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def bfs(node1,node2):
            if( not node1 and not node2):
                return None
            if(not node1 and node2):
                return node2
            if(not node2 and node1):
                return node1
            v1=node1.val if node1 else 0
            v2=node2.val if node2 else 0
            
            return TreeNode(v1+v2,bfs(node1.left,node2.left),bfs(node1.right,node2.right))
            
        return bfs(root1,root2)
            

        