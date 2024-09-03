# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)
      
        i = 0
        n = len(chalk)
      
        while chalk[i] <= k:
            k -= chalk[i]
            i += 1
                
        return i
        