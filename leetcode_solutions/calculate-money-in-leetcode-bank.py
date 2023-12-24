class Solution:
    def totalMoney(self, n: int) -> int:
        ans=0
        offset=0
        for i in range(1,n+1):
            res=i%7
            if res%7==0:
                res+=7
            ans+=offset+res
            if i%7==0:
                offset+=1
        return ans 