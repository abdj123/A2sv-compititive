# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        l = 0

        res = 0

        for r in range(len(nums)):
            while l <= r and nums[r] != mx:
                l += 1
            res = max(res, r - l + 1)
        return res