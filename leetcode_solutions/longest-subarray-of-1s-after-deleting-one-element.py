class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = prev = curr = 0

        for i in nums:
            if i:
                curr += 1
                longest = max(longest, prev + curr)
            else:
                prev, curr = curr, 0

        return longest - (longest == len(nums))