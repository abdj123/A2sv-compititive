class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res=float('inf')
        for i in range(len(blocks)-k+1):
            temp=blocks[i:i+k]
            res=min(res,temp.count("W"))
        return res
        