class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=[" "]*len(s)
        ans=""
        for i in range(len(indices)):
            res[indices[i]]=s[i]
        for i in res:
            ans+=i
        return ans