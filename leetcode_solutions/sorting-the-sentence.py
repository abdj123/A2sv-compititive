class Solution:
    def sortSentence(self, s: str) -> str:
        a=s.split(" ")
        output=""
        for i in range(10):
            for j in a:
                if(j[-1]==str(i)):
                    output+=f"{j[:-1]} "
        return output[:-1]
