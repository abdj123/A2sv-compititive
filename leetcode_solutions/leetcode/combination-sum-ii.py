class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        count=Counter(candidates)
        dct=defaultdict(int)
        con = list(set(candidates))
    
        def comb(ind,path,sum_):
            if(sum(path)==target):
                x=sorted(path)
                if(not x in res):
                    res.append(x)
                return
            if(sum_>target):
                return
            
            for i in range(ind,len(con)):
                if(dct[con[i]]<count[con[i]]):
                    path.append(con[i])
                    dct[con[i]]+=1
                    sum_+=con[i]
                    comb(i,path,sum_)
                    path.pop()
                    sum_-=con[i]
                    dct[con[i]]-=1      
        res=[]
        comb(0,[],0)
        return res
        