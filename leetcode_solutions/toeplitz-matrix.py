class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                if(j-i>=0 and matrix[i][j]!=matrix[0][j-i] or i-j>=0 and matrix[i][j]!=matrix[i-j][0]):
                    return False
        return True
                
        