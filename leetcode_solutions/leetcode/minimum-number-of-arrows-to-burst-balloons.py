class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        res=0
        rng=float("-inf")
        for start,end in points:
            if(start>rng):
                res+=1
                rng=end
        return res
        