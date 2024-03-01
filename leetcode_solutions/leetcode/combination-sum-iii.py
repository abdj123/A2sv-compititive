class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(ind,path):
            if(sum(path)==n and k==len(path)):
                res.append(path[:])
                return
            if(len(path) >= k):
                return
            
            for i in range(ind,10):
                path.append(i)
                backtrack(i+1,path)
                path.pop()

        res=[]
        backtrack(1,[])
        return res