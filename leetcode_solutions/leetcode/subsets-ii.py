class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        def rec(indx,path):
            if(indx==n):
                return
            for i in range(indx,n):
                path.append(nums[i])
                rec(i+1,path)
                x=sorted(path)
                if( not x in res):
                    res.append(x)
                path.pop()
        res=[[]]
        rec(0,[])
        return res
        