# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st = []
        
        for i in range(len(s)):
            if s[i] not in st:
                j = len(st) - 1
                
                while j >= 0 and st[j] > s[i] and st[j] in s[i + 1 :]:
                    st.pop()
                    j -= 1
                st.append(s[i])
        
        st = "".join(st)
        
        return st
