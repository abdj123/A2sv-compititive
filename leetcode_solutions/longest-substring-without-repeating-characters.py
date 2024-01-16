class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=float("-inf")
        i,j=0,0
        while(j<=len(s)):
            temp=s[i:j]
            if(len(set(temp))==j-i):
                res=max(res,j-i)
                j+=1
            else:
                i+=1
        return res
            
        