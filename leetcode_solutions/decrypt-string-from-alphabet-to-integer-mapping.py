class Solution:
    def freqAlphabets(self, s: str) -> str:
        res=""
        dict={}
        i=1
        for c in ascii_lowercase:
            if(i>9):
                dict[f"{i}#"]=c
            else:
                dict[f'{i}']=c
            i+=1
        j=len(s)-1
        while(j>=0):
            print(s[j])
            if(s[j]=="#"):
                temp=s[j-2:j+1]
                res+=dict[temp]
                j-=3
            else:
                res+=dict[s[j]]
                j-=1
        return res[::-1]
        