class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        cnt = 0
        
        answer = False
        for i in range(len(typed)):
            if cnt < len(name) and name[cnt] == typed[i]:
                cnt = cnt + 1
            elif i == 0 or typed[i] != typed[i-1]:
                return answer
            
        if cnt == len(name):
            answer = True
            
        return answer
