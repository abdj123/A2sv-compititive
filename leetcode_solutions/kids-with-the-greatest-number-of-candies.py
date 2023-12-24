class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx=max(candies)
        res=[]
        for i in candies:
            if(i+extraCandies>=mx):
                res.append(True)
            else:
                res.append(False)
        return res