class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res=0
        costs.sort(key=lambda x : x[0] - x[1])
        mid=len(costs)//2
        for i in range(mid):
            res+=costs[i][0]+costs[mid+i][1]
        print(costs)
        return res