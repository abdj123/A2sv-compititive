class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dct={}
        starts=[]
        res=[]
        
        for i,(a,b) in enumerate(intervals):
            dct[a]=i
            starts.append(a)
        starts.sort()
        
        for a,b in intervals:
            bisect=bisect_left(starts,b)
            if(b>starts[-1]):
                res.append(-1)
                continue
            res.append(dct[starts[bisect]])
        return res