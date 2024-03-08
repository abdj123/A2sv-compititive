class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def helper(mid):
            tot=0
            for i in nums:
                tot+=ceil(i/mid)
                if(tot>threshold):
                    return False
            return True
        l,r=1,max(nums)
        while(l<r):
            mid=(l+r)//2
            if helper(mid):
                r=mid
            else:
                l=mid+1
        
        return l
