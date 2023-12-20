class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        res=0
        if(n%2==0):
            return n
        else:
            return n*2
        