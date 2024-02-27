class Solution:
    def canJump(self, nums: List[int]) -> bool:
        good=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]+i>=good):
                good=i

        
        return good==0
        