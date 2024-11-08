# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n

        for i, word in enumerate(words):
            for ch in word:
                masks[i] |= 1 << (ord(ch) - ord("a"))

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))

        return res
