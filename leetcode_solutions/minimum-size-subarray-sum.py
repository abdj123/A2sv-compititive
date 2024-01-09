class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        prefix_sum = 0
        left = 0
        for right in range(len(nums)):
            prefix_sum += nums[right]
            while prefix_sum >= target:
                res = min(res, right - left + 1)
                prefix_sum -= nums[left]
                left += 1
        return res if res != float('inf') else 0
            
        