class Solution:
    def minimizedStringLength(self, s: str) -> int:
        temp=[]
        for i in s:
            temp.append(i)
        return len(set(temp))
        