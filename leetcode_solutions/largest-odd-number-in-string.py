class Solution:
    def largestOddNumber(self, num: str) -> str:
        res=""
        index=0
        for i in range(len(num)-1,-1,-1):
            if(eval(num[i])%2!=0):
                return num[:i+1]
        return ""
        