class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        res=[]
        
        for i in words:
            k=i.lower()
            flag=True
            temp=""
            if(k[0] in row1):
                temp=row1
            elif(k[0] in row2):
                temp=row2
            elif(k[0] in row3):
                temp=row3
            print(temp)
            print(k)
            for j in k[1:]:
                if(j not in temp):
                    flag=False
                    break
            if(flag):
                res.append(i)
                
        return res
        