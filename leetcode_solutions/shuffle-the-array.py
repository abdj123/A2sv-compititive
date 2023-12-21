class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[]
        i=0
        j=len(nums)//2
        while(j<len(nums)):
            res.append(nums[i])
            res.append(nums[j])
            i+=1
            j+=1
            
        return res
            
        