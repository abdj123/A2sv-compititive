class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n=len(matrix)
        m=len(matrix[0])
        self.prefix= [ [0]*(m+1) for i in range(n+1)]
        for i in range(n):
            tmp=0
            for j in range(m):
                tmp+=matrix[i][j]
                above=self.prefix[i][j+1]
                self.prefix[i+1][j+1]=tmp+above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,r2,c1,c2=row1+1,row2+1,col1+1,col2+1
        res=self.prefix[r2][c2]
        above=self.prefix[r1-1][c2]
        left=self.prefix[r2][c1-1]
        diagonal=self.prefix[r1-1][c1-1]

        return res-above+diagonal-left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)