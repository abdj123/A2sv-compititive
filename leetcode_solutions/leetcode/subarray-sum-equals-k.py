class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=curr=0
        prefix={0:1}
        for n in nums:
            curr+=n
            diff=curr-k
            res+=prefix.get(diff,0)
            prefix[curr]=1+prefix.get(curr,0)

        return res