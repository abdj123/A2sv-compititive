# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        _sum = sum(rolls)
        ln = n
        m = len(rolls)
        res = ((n + m) * mean) - _sum
        print(res)
        if res > n * 6 or res < 0 or res < n:
            return []
        div = res // n
        rem = res % n
        ans = [div] * n
        ind = 0
        for i in range(rem):
            ans[i] += 1
            ind += 1


        return ans
            
            

