class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        for i in range(len(words)):
            words[i] = ''.join([chr(order.index(words[i][j])) for j in range(len(words[i]))])

        return words == sorted(words)
        