class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        res=[]
        for i in count.keys():
            if(count[i]>len(nums)//3):
                res.append(i)
        return res
        