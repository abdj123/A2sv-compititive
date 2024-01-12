class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res=0
        # if(costs[0]>coins):
        #     return 0
        
        for i in range(len(costs)):
            if(coins-costs[i]>=0):
                res+=1
                coins-=costs[i]
        return res
        
