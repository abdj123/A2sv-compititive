class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        st=""
        a=sorted(strs)
        first=a[0]
        last=a[-1]

        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return st
            else:
                st+=first[i]
        return st
