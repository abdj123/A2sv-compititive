# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        back = False
        ind = 0
        
        for i in range(time):
            if ind == n - 1:
                back = True
            elif ind == 0:
                back = False
            
            if back:
                ind -= 1
            else:
                ind += 1
        
        return ind + 1
