class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[-1]*len(nums1)
        stack=[]
        dct={}

        for i in range(len(nums2)):
            while(stack and stack[-1]<nums2[i]):
                val=stack.pop()
                dct[val]=nums2[i]
            stack.append(nums2[i])
        
        for i in range(len(nums1)):
            res[i]=dct.get(nums1[i],-1)


        return res
