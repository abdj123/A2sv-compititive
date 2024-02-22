class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        k=3
        nums.sort()
        res=0
        print(nums)
        if(len(nums)<2):
            return 0
        for k in range(2,len(nums)):
            i,j=0,k-1
            while(i<j):
                if(nums[k]<nums[j]+nums[i]):
                    res+=(j-i)
                    j-=1
                else:
                    i+=1



        return res


        