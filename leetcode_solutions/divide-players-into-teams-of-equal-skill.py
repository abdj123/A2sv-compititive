class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill) 
        if n == 2: return skill[0] * skill[1]
        skill.sort()
        prev = None
        res = 0
        
        for i in range(n//2):
            j = n - i - 1
            
            if prev is None:
                prev = skill[i] + skill[j]
                res = skill[i] * skill[j]
            elif prev == skill[i] + skill[j]:
                res += skill[i] * skill[j]
            else: return -1
        
        return res

        
        