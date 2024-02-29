class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        left_sum=defaultdict(int)
        left_count=defaultdict(int)
        res=[0]*len(nums)

        for i,v in enumerate(nums):
            res[i]+=left_count[v]*i
            res[i]-=left_sum[v]

            left_count[v]+=1
            left_sum[v]+=i

        right_sum=defaultdict(int)
        right_count=defaultdict(int)

        for i,v in reversed(list(enumerate(nums))):
            
            res[i]+=right_sum[v]
            res[i]-=right_count[v]*i

            right_count[v]+=1
            right_sum[v]+=i
        return res

        return []
        