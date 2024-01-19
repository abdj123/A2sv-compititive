class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix=0
        res=[]
        for i in nums:
            prefix+=i
            res.append(prefix)
        return res