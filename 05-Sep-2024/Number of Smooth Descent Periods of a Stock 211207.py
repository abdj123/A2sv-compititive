# Problem: Number of Smooth Descent Periods of a Stock - https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        stack = []
        res = 0
        n = len(prices)
        for i in range(n):
            if stack and (stack[-1] <= prices[i] or (stack[-1] - prices[i]) > 1):
                stack = []
            if not stack or (stack[-1] - prices[i]) == 1:
                stack.append(prices[i])
                res += len(stack)
        return res
