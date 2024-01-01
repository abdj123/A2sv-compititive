class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        ans = []

        for key, value in count1.items():
            if key in count2:
                minval = min(value, count2[key])

                for _ in range(minval):
                    ans.append(key)

        return ans