class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row={}
        col={}
        res=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if(i not in row):
                    row[i]=grid[i][j]
                if(j not in col):
                    col[j]=grid[i][j]
                row[i]=max(row[i],grid[i][j])
                col[j]=max(col[j],grid[i][j])
        for i in range(len(grid)):
            for j in range(len(grid)):
                m=min(row[i],col[j])
                if(m>grid[i][j]):
                    res+=(m-grid[i][j])
        return res

        