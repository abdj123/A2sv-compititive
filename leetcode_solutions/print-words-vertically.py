class Solution:
    def printVertically(self, s: str) -> List[str]:
        return map(str.rstrip, map(''.join, zip_longest(*s.split(), fillvalue=' ')))

        