class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d= {}
        sumou=0
        for  i in answers:
            if i==0:
                 sumou+=i+1
            elif i not in d:
                sumou+=i+1
                d[i]=1
            else:
                if d[i]>i:
                     sumou+=i+1
                     d[i]=1
                else:
                    d[i]=d[i]+1  
                   
        return sumou
        