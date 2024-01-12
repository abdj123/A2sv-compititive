class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res=0
        n=len(nums)-1
        
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]<nums[i+1]):
                res+=n-i
        return res
    