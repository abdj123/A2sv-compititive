class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dist=len(set(nums))
        res,n=0,len(nums)
        dct=defaultdict(int)
        l=0
        
        for i in range(n):
            dct[nums[i]]+=1
            while(dist==len(dct)):
                res+=n-i
                dct[nums[l]]-=1
                if(not dct[nums[l]]):
                    dct.pop(nums[l])
                l+=1
            
        
        return res

                
            
        