class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        res=0
        sum_=0
        count={}
        for r in range(len(nums)):
            count[nums[r]]=count.get(nums[r],0)+1
            while(count[nums[r]]>1):
                count[nums[l]]-=1
                sum_-=nums[l]
                l+=1
            sum_+=nums[r]
            res=max(res,sum_)
        return res