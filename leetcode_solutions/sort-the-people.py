class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        hash=dict()
        res=[]
        
        for n, h in zip(names,heights):
            hash[h]=n
        
        heights.sort()
        for val in heights:
            res.append(hash[val])
        
        return res[::-1]