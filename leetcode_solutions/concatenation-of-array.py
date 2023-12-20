class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res=nums
        res.extend(nums)
        return res
        