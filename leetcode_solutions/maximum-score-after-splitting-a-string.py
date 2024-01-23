class Solution:
    def maxScore(self, s: str) -> int:
        total=s.count("1")
        ones=total
        res=0
        zero=0
        for i in range(len(s)-1):
            if(s[i]=="0"):
                zero+=1
            else:
                ones-=1
            res=max(res,zero+ones)
        return res
            