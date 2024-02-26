class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def comb(start):
            if(len(path)==k):
                res.append(path[:])
                return
            if start > n:
                return
            path.append(start)
            comb(start+1)
            path.pop()
            comb(start+1)

            
        res=[]
        path=[]
        comb(1)
        return res
             