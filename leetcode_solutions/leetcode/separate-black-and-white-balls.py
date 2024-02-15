class Solution:
    def minimumSteps(self, s: str) -> int:
        zero=0
        if(len(s)==1):
            return 0
        n=len(s)
        j=0
        res=0
        zeros=0
        
        while(j<n):
            if(s[j]=="0"):
                res+=j-zeros
                zeros+=1

            j+=1
        return res
        