class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        equal=[]
        less=[]
        above=[]
        for i in nums:
            if(i>pivot):
                above.append(i)
            elif(i<pivot):
                less.append(i)
            elif(i==pivot):
                equal.append(i)
        return less+equal+above