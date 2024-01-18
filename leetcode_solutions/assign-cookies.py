class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res=0
        i=j=0
        while(i<len(g) and j<len(s)):
            if(g[i]>s[j]):
                j+=1
            elif(s[j]>=g[i]):
                res+=1
                i+=1
                j+=1
        return res
                