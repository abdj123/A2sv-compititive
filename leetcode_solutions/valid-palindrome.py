class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=""
        for i in s.lower():
            if(i.isalnum()):
                temp+=i
        return temp==temp[::-1]
        