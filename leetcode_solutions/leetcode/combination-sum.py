class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        def comb(ind,path):
            if(sum(path)==target):
                x=sorted(path)
                if(not x in res):
                    res.append(x)
                return
            if(sum(path)>target):
                return
            for i in range(n):
                path.append(candidates[i])
                comb(i+1,path)
                path.pop()
        
        res=[]
        comb(0,[])
        return res