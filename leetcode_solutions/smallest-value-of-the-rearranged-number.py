class Solution:
    def smallestNumber(self, num: int) -> int:
        if(num<0):
            st=str(num)
            st=sorted(st,reverse=True)
            res="-"
            for i in st[:-1]:
                res+=i
            
            return eval(res)
        else:
            st=str(num)
            st=sorted(st)
            lead=""
            got=False
            res=""
            for i in st:
                if(i!="0" and not got):
                    lead=i
                    got=True
                else:
                    res+=i
            res=lead+res
            return eval(res)
            