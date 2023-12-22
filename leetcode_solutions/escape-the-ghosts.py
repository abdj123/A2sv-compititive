class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mine=abs(target[0])+abs(target[1])
        for i in ghosts:
            ghost=abs(i[0]-target[0])+abs(i[1]-target[1])
            
            if(mine>=ghost):
                return False
        return True
        