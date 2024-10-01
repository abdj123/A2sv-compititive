# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = sorted(heights)

        res = 0

        for a,b in zip(temp, heights):
            if a != b:
                res += 1
        return res