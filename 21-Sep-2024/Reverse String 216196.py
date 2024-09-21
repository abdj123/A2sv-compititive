# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s) - 1
        i = 0

        def swap(i, j):
            if i <= j:
                s[i], s[j] = s[j], s[i]
                j -= 1
                i += 1
                swap(i, j)

        swap(i, j)
