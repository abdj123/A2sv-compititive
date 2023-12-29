class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        
        for i in zip(*strs):
            if(sorted(i)!=list(i)):
                count+=1
                
                
        return count
        