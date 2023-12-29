class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        
        if(len(strs[0])==1):
            if(sorted(strs)==strs):
                return 0
            else:
                return 1
        
        for i in range(len(strs[0])):
            st=""
            for j in range(len(strs)):
                st+=strs[j][i]
            
            print(st)
            if(list(st)!=sorted(st)):
                count+=1
        
        return count
        