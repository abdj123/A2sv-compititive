class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch != ')':
                stack.append(ch)
            else:
                num = []
                while stack and stack[-1] != '(':
                    num.append(int(stack.pop()))
                stack.pop()
                num = max(1,sum(num)*2)
                stack.append(num)
        return sum(stack)