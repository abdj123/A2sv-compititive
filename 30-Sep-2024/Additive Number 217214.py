# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def backtrack(ind):
            if ind == n:
                if len(path) >= 3 and len("".join(map(str, path))) == n:
                    return True
                return False
            for i in range(ind, n):
                temp = int(num[ind : i + 1])
                if len(path) < 2 or (path[-2] + path[-1]) == temp:
                    path.append(temp)
                    res = backtrack(i + 1)
                    path.pop()
                    if res:
                        return True
            return False

        path = []
        return backtrack(0)
