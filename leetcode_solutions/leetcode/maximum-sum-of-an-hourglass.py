class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        res=0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                upper=sum(grid[i][j:j+3])
                mid=grid[i+1][j+1]
                bottom=sum(grid[i+2][j:j+3])
                res=max(res,(upper+mid+bottom))
                

        return res