class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        path=path.split('/')
        for i in path:
            if stack and i=='..':
                stack.pop()
            elif i not in ['.','','..']:
                stack.append(i)
        return '/'+'/'.join(stack)