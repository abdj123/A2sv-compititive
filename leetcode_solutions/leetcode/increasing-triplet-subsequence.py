class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left=right=float('inf')
        for num in nums:
            if(num<=left):
                left=num
            elif(num<=right):
                right=num
            else:
                return True
        return False