class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        i=len(tasks)-1
        res=0
        
        for p in processorTime:
            res=max(res,p+tasks[i])
            i-=4
        return res