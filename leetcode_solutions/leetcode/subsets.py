class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def rec(start,path):
            if(len(path)==len(nums)):
                return
            for i in range(start,len(nums)):
                if(nums[i] not in path):
                    path.append(nums[i])
                    rec(i,path)
                    res.append(path[:])
                    path.pop()
        res=[[]]
        rec(0,[])
        res.sort()

        return res