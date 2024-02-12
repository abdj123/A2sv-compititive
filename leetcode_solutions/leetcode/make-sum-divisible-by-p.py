class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums) % p
        if remainder == 0:
            return 0
        prefixToIndex = {0: -1}
        prefixSum = 0
        ans = len(nums)
        for i, num in enumerate(nums):
            prefixSum = (prefixSum + num) % p
            target = (prefixSum - remainder + p) % p 
            if target in prefixToIndex:
                ans = min(ans, i - prefixToIndex[target])
            prefixToIndex[prefixSum] = i
        
        return -1 if ans == len(nums) else ans