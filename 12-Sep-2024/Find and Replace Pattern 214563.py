# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def numify(word):
            seen = defaultdict(int)
            count = ord('a')
            pattern = []
            for char in word:
                if seen[char]:
                    pattern.append(seen[char])
                else:
                    seen[char] = chr(count)
                    pattern.append(chr(count))
                    count += 1
                
            return ''.join(pattern)

        new_pattern = numify(pattern)
        result = []
        for word in words:
            x = numify(word)
            if x == new_pattern:
                result.append(word)
        return result