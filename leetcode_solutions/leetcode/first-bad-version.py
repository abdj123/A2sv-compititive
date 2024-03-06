# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while(left <= right):
            mid=left + (right - left) // 2
            if(not isBadVersion(mid)):
                left = mid + 1
            elif(isBadVersion(mid)):
                right = mid - 1
        return left
        
        