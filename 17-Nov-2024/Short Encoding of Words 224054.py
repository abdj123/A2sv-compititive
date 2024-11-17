# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        rev_words = list(map(lambda x: x[::-1], words))
        rev_words_list = sorted([word for i, word in enumerate(rev_words)])[::-1]
        ans = [rev_words_list[0]]
        for j in range(1, len(rev_words_list)):
            if rev_words_list[j - 1].startswith(rev_words_list[j]):
                continue
            else:
                ans.append(rev_words_list[j])
        num = len(ans)
        for j in ans:
            num = num + len(j)
        return num