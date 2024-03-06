class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        for i in range(len(nums)):
            if(nums[i]==target):
                return i