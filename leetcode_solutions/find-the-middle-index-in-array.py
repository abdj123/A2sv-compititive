class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        prefix=0
        for i in range(len(nums)):
            if(sum(nums[:i])==sum(nums[i+1:])):
                return i
            
        return -1