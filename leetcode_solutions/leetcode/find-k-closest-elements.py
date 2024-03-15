class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        temp=[]
        res=[]
        
        for i in arr:
            temp.append([abs(i-x),i])
        temp.sort()
        
        for i in range(k):
            res.append(temp[i][1])
        res.sort()
        
        return res
        