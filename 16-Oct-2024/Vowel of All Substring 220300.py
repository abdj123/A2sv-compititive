# Problem: Vowel of All Substring - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        vowls = "aeiou"
        res = 0
        n = len(word)

        for i,v in enumerate(word):
            if v in vowls:
                res += (i + 1) * (n - i)
        
        return res