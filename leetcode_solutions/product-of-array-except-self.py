class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if(nums.count(0)>1):
            return [0]*len(nums)
        
        total=1
        nozero=1
        
        for i in nums:
            if(i!=0):
                nozero*=i
            total*=i
        
        res=[]
        for i in nums:
            if(i==0):
                res.append(nozero)
            else:
                res.append(total//i)
        
        return res