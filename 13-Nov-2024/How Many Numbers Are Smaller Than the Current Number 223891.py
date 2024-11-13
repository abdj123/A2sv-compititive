# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        prefix = [0]
        for i in range(max(freq.keys())):
            prefix.append(freq.get(i, 0) + prefix[-1])
        return [prefix[num] for num in nums]
