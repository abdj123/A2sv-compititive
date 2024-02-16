class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        calls = [0] * len(nums)
        for s, e in requests:
            calls[s] += 1
            if e + 1 < len(nums):
                calls[e+1] -= 1 
        
        total = 0
        for idx, val in enumerate(calls):
            total += val
            calls[idx] = total
        calls.sort()
        nums.sort()
        res = 0
        l, r = len(nums) - 1 , len(calls) - 1
        while r > -1:
            res += calls[r] * nums[l]
            l -= 1
            r -= 1
        return res % (10 ** 9 + 7)