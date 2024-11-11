# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        res = ""

        for i in s:
            if stack and stack[-1][0] == i:
                stack[-1][1] = stack[-1][1] + 1
            else:
                stack.append([i, 1])
            
            if stack and stack[-1][1] == k:
                stack.pop()

        for c, v in stack:
            res += (c * v)
        
        return res