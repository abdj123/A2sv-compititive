# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        st = set()
        
        for i in nums:
            if i not in st and i > 0:
                st.add(i)
        nums = sorted(list(st))
        st.clear()
        
        if not nums:
            return 1
        
        if nums and nums[0] > 1:
            return 1
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                return nums[i - 1] + 1
        
        return nums[-1] + 1
