# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        heap = []
        
        for i in nums:
            heapq.heappush(heap, -i)
        
        for i in range(k):
            val = heapq.heappop(heap)
            val = -val
            res += val
            temp = ceil(val / 3)
            heapq.heappush(heap, -temp)

        return res