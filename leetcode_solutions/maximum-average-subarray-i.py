class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum=max_sum=sum(nums[:k])
        for i in range(k,len(nums)):
            curr_sum+=(nums[i]-nums[i-k])
            max_sum=max(max_sum,curr_sum)
        return max_sum/k