class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]<=nums[i+1]):
                continue
            slots = ceil(nums[i]/nums[i+1])
            res += slots - 1
            nums[i]=nums[i] // slots
        
        return res
        