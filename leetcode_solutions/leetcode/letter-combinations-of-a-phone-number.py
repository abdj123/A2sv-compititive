class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(not digits):
            return []
        
        dct={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        st=""
        for i in digits:
            st+=dct[i]
        n=len(digits)
        
        def backtrack(ind,path):
            if(len(path)==n):
                res.append("".join(path))
                return
            if(ind>=len(st)):
                return
            if(len(path)>=n):
                return
            for i in range(ind,n):
                for j in dct[digits[i]]:
                    path.append(j)
                    backtrack(i+1,path)
                    path.pop()
        
        res=[]
        backtrack(0,[])
        return res
        