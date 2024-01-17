class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        checked=set()
        for i in range(len(nums)):
            if(i not in checked):
                cycle=set()
                while True:
                    if(i in cycle):
                        return True
                    checked.add(i)
                    cycle.add(i)
                    j,i=i,(i+nums[i])%len(nums)
                    
                    if(j==i):
                        break
                    if(nums[j]>0!=nums[i]<0):
                        break
        return False
    