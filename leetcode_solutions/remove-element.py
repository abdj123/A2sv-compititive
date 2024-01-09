class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j=0,len(nums)-1
        res=0
        while(j>i):
            if(val==nums[j]):
                 while(nums[j]==val and j>i):
                    j-=1
            if(val==nums[i]):
                nums[j],nums[i]=nums[i],nums[j]
            
            i+=1
        for i in nums:
            if(val!=i):
                res+=1
        return res