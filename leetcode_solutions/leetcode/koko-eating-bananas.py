class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid=(left+right)//2
            curr=0
        
            for i in piles:
                curr += ceil(i/mid)
            if curr > h:
                left = mid + 1
            else:
                right = mid - 1
        return left