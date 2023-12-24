class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {num: i for i, num in enumerate(nums)}
        for s, e in operations:
            i = dic[s]
            nums[i] = e
            dic[e] = i
            del dic[s]
        return nums
        