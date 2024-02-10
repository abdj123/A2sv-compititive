class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res=0
        prefix=[0]
        for i in nums:
            prefix.append(prefix[-1]+i)
        dct=defaultdict(int)
        for i in range(len(prefix)):
            diff=prefix[i]-goal
            res+=dct[diff]
            dct[prefix[i]]+=1
        return res