class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=j=0
        res=0
        while(j<len(nums)):
            
            if(nums[j]==0):
                j+=1
                i=j
            else:
                res=max(res,(j-i)+1)
                j+=1
        return res
            
        