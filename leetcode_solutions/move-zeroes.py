class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        c=nums.count(0)
        
        for i in range(c):
            nums.remove(0)
        for i in range(c):
            nums.append(0)