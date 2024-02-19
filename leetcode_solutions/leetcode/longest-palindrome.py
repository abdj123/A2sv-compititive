class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        print(count)
        res=0
        odd=[]
        for v in count.values():
            if(v%2==0):
                res+=v
            else:
                odd.append(v)

        odd.sort()
        c=0
        for i in odd[::-1]:
            if(not c):
                res+=i
                c+=1
            else:
                res+=(i-1)
        return res
        