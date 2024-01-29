class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arrLength = len(nums)

        nums.sort()

        ans = []

        for idx in range(0, arrLength):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            start, end = idx + 1, arrLength - 1
            
            while start < end:
                threeSum = nums[idx] + nums[start] + nums[end]

                if threeSum == 0:
                    ans.append([nums[idx], nums[start], nums[end]])
                
                    while (start < end) and nums[start] == nums[start + 1]:
                        start += 1
                    
                    while (start < end) and nums[end] == nums[end - 1]:
                        end -= 1

                    start += 1
                    end -= 1

                elif threeSum < 0:
                    start += 1
                
                else:
                    end -= 1

        return ans