class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        temp1=""
        temp2=""
        for i in word1:
            temp1+=i
        for j in word2:
            temp2+=j
        return temp1==temp2
        