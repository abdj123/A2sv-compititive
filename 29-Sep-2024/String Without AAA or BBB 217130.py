# Problem: String Without AAA or BBB - https://leetcode.com/problems/string-without-aaa-or-bbb

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = ''
        while a or b:
            if len(ans) >= 2 and ans[-1] == ans[-2]: WA = ans[-1] == 'b'
            else: WA = a >= b
            if WA:
                a -= 1
                ans += 'a'
            else:
                b -= 1
                ans += 'b'
        return ans