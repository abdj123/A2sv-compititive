class Solution:
    def numberOfMatches(self, n: int) -> int:
        res=0
        while(n!=1):
            if(n%2==0):
                n=n//2
                res+=n
            else:
                res+=(n-1)//2
                n=(n+1)//2
        return res