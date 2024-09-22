# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        n = len(start)
        l = 0
        r = start[-1] - start[0] + d + 1

        def isPossible(score: int) -> bool:
            pre = start[0]
            for i in range(1, n):
                if start[i] + d - pre < score:
                    return False
                pre = max(start[i], pre + score)
            return True

        while l < r:
            m = l + (r - l) // 2
            if isPossible(m):
                l = m + 1
            else:
                r = m
        return l - 1