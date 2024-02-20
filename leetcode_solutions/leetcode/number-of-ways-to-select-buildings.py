class Solution:
    def numberOfWays(self, s: str) -> int:
        n=len(s)
        res=0
        seen=[[0]*2 for _ in range(2)]

        for i in range(n):
            curr=int(s[i])
            res+=seen[1][1-curr]
            seen[1][curr]+=seen[0][1-curr]
            seen[0][curr]+=1

        return res