class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        
        for i in range(n):
            count=0
            for j in range(n):
                if(nums[i]>nums[j] and i!=j):
                    count+=1
            res.append(count)
        
        return res