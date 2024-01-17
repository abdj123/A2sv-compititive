class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        k=len(p)
        count=Counter(p)
        anag=Counter(s[:k])
        if(count==anag): res.append(0)
        for i in range(k,len(s)):
            anag[s[i-k]]-=1
            if(anag[s[i-k]]==0):
                anag.pop(s[i-k])
            anag[s[i]]+=1
            if(count==anag):
                res.append(i-k+1)
        return res
        