# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ""
        ls = [str(ord(i) - 96) for i in s]
        
        for i in ls:
            res += i
        prev = res
        
        for i in range(k):
            temp = 0
            for j in str(res):
                temp += int(j)
            res = temp
            if res == prev:
                return res
            prev = res
        
        return res
