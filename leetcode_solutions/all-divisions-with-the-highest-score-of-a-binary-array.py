class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        if(len(nums)==sum(nums)):
            return [0]
        i=0
        res=[]
        psum=0
        total=sum(nums)
        
        one=nums.count(1)
        res.append(one)
        while(i<len(nums)):
            psum+=nums[i]
            lsum=(i+1)-(psum)
            rsum=total-psum
            sum_=lsum+rsum
            res.append(sum_)
            i+=1
        
        ans=[]
        print(res)
        max_=max(res)
        for i in range(len(res)):
            if(res[i]==max_):
                ans.append(i)
        return ans