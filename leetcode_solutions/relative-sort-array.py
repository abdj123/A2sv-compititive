class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res=[]
        out=[]
        
        for i in arr2:
            for j in arr1:
                if(i==j):
                    res.append(j)
        for i in arr1:
            if(i not in arr2):
                out.append(i)
        out.sort()
        return res+out