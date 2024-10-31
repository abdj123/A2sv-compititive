# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        res = 0
        for i in range(n):
            if stack and stack[-1][0] > nums[i]:
                stack.append([nums[i], i])
            elif not stack:
                stack.append([nums[i], i])
        
        for i in range(n - 1, -1, -1):
            while stack and stack[-1][0] <= nums[i]:
                val = stack.pop()
                res = max(res, (i - val[1]))


        return res