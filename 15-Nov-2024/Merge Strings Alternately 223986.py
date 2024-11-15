# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        res = []
        n, m = len(word1), len(word2)
        while i < n and j < m:
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.extend(word1[i:])
        res.extend(word2[j:])

        return "".join(res)