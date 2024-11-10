# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        i, j = 0, n - 1
        res = 0

        while i <= j:
            curr = 0
            if people[j] <= limit:
                curr += people[j]
                j -= 1
            if curr + people[i] <= limit:
                curr += people[i]
                i += 1
            if curr > 0:
                res += 1
        return res