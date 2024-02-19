class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if(target==1):
            return 0
        res=1
        rem=0
        count=0
        n=target
        for i in range(maxDoubles):
            rem+=(n%2)
            count+=1
            n=n//2
            if(n==1):
                break
        return n+rem+count-1

        