class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set_=set(nums1)&set(nums2)
        tmp=list(set_)
        if(len(tmp)==0):
            return -1
        else:
            return min(tmp)
        