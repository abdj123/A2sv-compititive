# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr=[]
        def preorder(root):
            if(not root):
                return
            preorder(root.left)
            arr.append(root.val)
            preorder(root.right)
        preorder(root)
        def generate(arr):
            if not arr:
                return 
            mid=len(arr)//2
            root=TreeNode(arr[mid])
            root.left=generate(arr[:mid])
            root.right=generate(arr[mid+1:])

            return root
        return generate(arr)
            