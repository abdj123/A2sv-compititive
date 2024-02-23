class Solution:
    def decodeString(self, s: str) -> str:
        res=""
        stack=[]
        for i in range(len(s)):
            tmp=""
            inner=False
            while(stack and stack[-1]!="[" and s[i]=="]"):
                val=stack.pop()
                tmp=val+tmp
                inner=True
                print(tmp)
            if(stack and inner):
                stack.pop()
                num=""
                while(stack and stack[-1].isdigit()):

                    num=stack.pop()+num
                print(num)
                tmp=tmp*int(num)
                stack.append(tmp)
            if(s[i]=="]"):
                continue
            
            stack.append(s[i])
        return "".join(stack)
