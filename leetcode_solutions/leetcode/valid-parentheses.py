class Solution:
    def isValid(self, s: str) -> bool:
        valid={"}":"{",")":"(","]":"["}
        stack=[]
        for i in s:
            if(i in valid.values()):
                stack.append(i)
            elif(stack and stack[-1]==valid[i]):
                stack.pop()
            else:
                return False
        
        return 0==len(stack)
        