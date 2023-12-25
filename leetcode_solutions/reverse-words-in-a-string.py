class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        st=s.split()
        for i in st:
            if(i!=" "):
                res.append(i)
        ans=""
        for i in res[::-1]:
            ans+=f" {i}"
        return ans[1:]