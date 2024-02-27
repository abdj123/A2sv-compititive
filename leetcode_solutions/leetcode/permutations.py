class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        def backtrack(ind,path,cand):
            if(len(path)==n):
                res.append(path[:])
                return
            for i in range(0,len(cand)):
                path.append(cand[i])
                backtrack(i+1,path,cand[:i]+cand[i+1:])
                path.pop()
        res=[]
        backtrack(0,[],nums)
        return res