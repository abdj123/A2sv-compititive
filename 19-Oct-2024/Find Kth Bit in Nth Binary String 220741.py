# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, N: int, K: int, R=True) -> str:
        if K == 1:
            return "0" if R else "1"
        mid = 1 << (N - 1)
        if K < mid:
            return self.findKthBit(N - 1, K, R)
        if K > mid:
            return self.findKthBit(N - 1, 2 * mid - K, not R)
        return "1" if R else "0"
