# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(
        self, nums: List[int], indexDifference: int, valueDifference: int
    ) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n):
                indx = abs(i - j)
                val = abs(nums[i] - nums[j])
                if indx >= indexDifference and val >= valueDifference:
                    return [i, j]
        return [-1, -1]
