class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res=[]
        i,j=0,1
        while(j<len(nums)):
            temp=[nums[j] for i in range(nums[i])]
            res.extend(temp)
            j+=2
            i+=2
        return res
        