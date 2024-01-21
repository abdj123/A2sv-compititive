class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closet = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if sum3 < target:
                    l += 1
                else:
                    r -=1
                if abs(sum3 - target) < abs(closet - target):
                    closet = sum3
        return closet