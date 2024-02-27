class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def comb(indx,path):
            if(len(path)==k):
                res.append(path[:])
                return 
            for i in range(indx,n+1):
                path.append(i)
                comb(i+1,path)
                path.pop()
        res=[]
             
        comb(1,[])
        return res