class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        res=0
        
        for i in range(1,len(points)):
            temp=points[i][0]-points[i-1][0]
            res=max(res,temp)
        
        return res