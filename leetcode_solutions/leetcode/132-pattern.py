class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        third=float('-inf')
        nums.reverse()
        for i in nums:
            if(i<third):
                return True
            while(stack and i>stack[-1]):
                third=stack.pop()
            stack.append(i)
        return False