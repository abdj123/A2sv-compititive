# Problem: Remove Duplicates from Sorted Array II - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dct = defaultdict(int)
        count = 0
        n = len(nums)
        

        for i in range(n):
            if dct[nums[i]] < 2:
                dct[nums[i]] += 1
                count += 1
            else:
                nums[i] = inf

        nums.sort()


        return count

        
