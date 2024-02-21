class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dct={}
        stack=[]
        
        for i,v in enumerate(temperatures):
            while(stack and v>stack[-1][1]):
                val=stack.pop()
                dct[val[0]]=i-val[0]
            stack.append([i,v])

        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            res[i]=dct.get(i,0)
        
        return res

        