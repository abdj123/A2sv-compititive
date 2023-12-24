class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        idx = 0
        n = len(spaces)
        
        for i in range(len(s)):
            space_idx = spaces[idx]
            if(i == space_idx):
                res += " "
                if(idx != n - 1): idx += 1 
            res += s[i]
                
        return res