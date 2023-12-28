class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans=[]
        n=len(matrix)
        for i in range(n):
            temp=[]
            for j in range(n):
                temp.append(matrix[j][i])
            ans.append(temp[::-1])
        
        for i in range(n):
            matrix[i]=ans[i]
            