class Solution:
    def isHappy(self, n: int) -> bool:
        if(n==1): return True
        temp=[]
        while(n!=1):
            t=str(n)
            summ=0
            if(n in temp): return False
            for i in range(len(t)):
                summ+=int(t[i])**2
            if(summ==1):
                return True
            temp.append(n)
            n=summ
        return False
        