class NumArray:

    def __init__(self, nums: List[int]):

        self.prefixsum=[]
        cursum=0
        for i in nums:
            cursum+=i
            self.prefixsum.append(cursum)
        #return self.prefixsum
        

    def sumRange(self, left: int, right: int) -> int:
        if(left==0):
            return self.prefixsum[right]
        else: return self.prefixsum[right]-self.prefixsum[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)