class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        res=[]
        for k,v in count.items():
            if(v==2):
                res.append(k)
        return res