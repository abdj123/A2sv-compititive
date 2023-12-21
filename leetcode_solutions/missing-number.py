class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=len(nums)
        res=0
        for i in range(1,a+1):
            if(i not in nums):
                res=i
                break
        return res