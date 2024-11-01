# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        res = 0
        temp = max(nums)
        for i in range(k):
            res += temp
            temp += 1
        return res
