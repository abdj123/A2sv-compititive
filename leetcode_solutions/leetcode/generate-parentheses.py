class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def validate(st):
            stack=[]
            for i in st:
                if(stack and stack[-1]=="(" and i==")"):
                    stack.pop()
                    continue
                else:
                    stack.append(i)
            return len(stack)==0
        def backtrack(ind,path):
            temp="".join(path[:])
            if(len(path)==(2*n)):
                if(validate(temp)):
                    res.append(temp)
                return
            print(path)
            for i in range(len(s)):
                path.append(s[i])
                backtrack(i+1,path)
                path.pop()
        res=[]
        s="()"
        backtrack(0,[])
        return res

        