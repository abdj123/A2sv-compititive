class Solution:
    def maxConsecutiveAnswers(self, answer: str, k: int) -> int:
        n=len(answer)
        res=0
        for i in ["T","F"]:
            count=0
            l=0
            for r in range(n):
                if(i!=answer[r]):
                    count+=1
                while(k<count):
                    if(answer[l]!=i):
                        count-=1
                    l+=1
                res=max(res,r-l+1)
        return res
                
