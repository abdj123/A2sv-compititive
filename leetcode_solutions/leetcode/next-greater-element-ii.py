class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        res=[-1]*len(nums)
        n=len(nums)
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()]=nums[i]

            stack.append(i)
        print(res,stack)
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()]=nums[i]
        return res