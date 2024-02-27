class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={}
        for i,v in enumerate(s):
            last[v]=i
        res=[]
        size,end=0,0
        for i, v in enumerate(s):
            size+=1
            end=max(end, last[v])
            if(i==end):
                res.append(size)
                size=0
        
        return res
        