class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        
        n=len(flips)
        temp=0
        res=0
        
        
        for i in range(n):
            temp=max(temp,flips[i])
            if(temp==(i+1)):
                res+=1

        return res

        
        
        