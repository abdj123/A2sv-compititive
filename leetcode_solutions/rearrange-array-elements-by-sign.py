class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[i for i in nums if i>0]
        neg=[i for i in nums if i<0]
        res=[]
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res