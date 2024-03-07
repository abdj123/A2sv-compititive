# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def bfs(root):
            if(not root):
                return
            que=deque([root])
            
            while(len(que)>0):
                
                temp=[]
                for i in range(len(que)):

                    node = que.popleft()
                    temp.append(node.val)

                    if(node.left):
                        que.append(node.left)
                    if(node.right):
                        que.append(node.right)
                
                if(len(res)%2):
                    temp.reverse()
                res.append(temp)
            
        bfs(root)
        return res
        