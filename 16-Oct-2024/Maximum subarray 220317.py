# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        res = nums[0]

        for i in nums[1:]:
            curr = max(i + curr, i)
            res = max(res, curr)

        return res