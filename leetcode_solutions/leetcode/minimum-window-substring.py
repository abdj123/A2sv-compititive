class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t) or t == "":
            return ""
        
        count=Counter(t)
        dct=defaultdict(int)
        l=0
        have,need=0,len(count)
        res,res_len=[-1,-1],float("inf")
        
        for i in range(len(s)):
            dct[s[i]]+=1
            if(count[s[i]] > 0 and dct[s[i]]==count[s[i]]):
                have+=1
            while(have == need):
                temp = (i - l + 1)
                if temp < res_len:
                    res=[l,i]
                    res_len = temp
                dct[s[l]]-=1
                if count[s[l]] > 0 and dct[s[l]] < count[s[l]]:
                    have-=1
                l+=1
        
        return s[res[0]:res[1]+1]