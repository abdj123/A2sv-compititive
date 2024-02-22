class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        curr=res=nums[0]
        for i in range(1,len(nums)):
            curr+=nums[i]
            tmp=curr/(i+1)
            res=max(res,math.ceil(tmp))
        return res