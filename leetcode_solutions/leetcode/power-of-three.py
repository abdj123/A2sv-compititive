class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<=0): return False
        else:
            return (math.log10(n) / math.log10(3)) % 1 == 0