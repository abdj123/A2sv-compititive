class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        if(len(palindrome)==1):
            return ""
        count_a=palindrome.count("a")
        if(count_a==len(palindrome) or count_a==len(palindrome)-1):
            return palindrome[:-1]+"b"
        # elif():

        
        i=0
        res=""
        count=0
        while(i<len(palindrome)):
            if(count==0 and palindrome[i]!="a"):
                count+=1
                res+="a"
                i+=1
                continue
            res+=palindrome[i]
            i+=1
        return res
        