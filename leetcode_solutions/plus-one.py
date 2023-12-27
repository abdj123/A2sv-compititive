class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s+=str(i)
        s+="+1"
        temp=str(eval(s))
        res=[]
        for val in temp:
            res.append(int(val))
        return res