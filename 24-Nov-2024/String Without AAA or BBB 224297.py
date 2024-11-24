# Problem: String Without AAA or BBB - https://leetcode.com/problems/string-without-aaa-or-bbb

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        while a > 0 or b > 0:
            if a > b:
                if len(res) >= 2 and res[-1] == res[-2] == 'a':
                    res.append('b')
                    b -= 1
                else:
                    res.append('a')
                    a -= 1
            else:
                if len(res) >= 2 and res[-1] == res[-2] == 'b':
                    res.append('a')
                    a -= 1
                else:
                    res.append('b')
                    b -= 1
        
        return ''.join(res)