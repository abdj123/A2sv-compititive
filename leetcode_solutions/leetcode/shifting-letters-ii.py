class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix=[0]*(len(s)+1)
        res=""
        orda=ord('a')

        for f,e,d in shifts:
            if(d==1):
                prefix[f]+=1
                prefix[e+1]-=1
            else:
                prefix[f]-=1
                prefix[e+1]+=1
        
        for i in range(1,len(prefix)):
            prefix[i]+=prefix[i-1]
        
        for i in range(len(prefix)-1):
            temp=(ord(s[i])-orda+prefix[i])%26
            res+=chr(temp+orda)
        
        return res
        

        