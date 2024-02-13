class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=sum(nums)
        print(total)
        temp=0
        for i in range(len(nums)):
            temp+=nums[i]
            total=max(total,temp)
            if(temp<0):
                temp=0
        return total