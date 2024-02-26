class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]

        for i in permutations(nums):
            res.append(i)
        return res