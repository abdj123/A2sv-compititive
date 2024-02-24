class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        countD=senate.count("D")
        countR=senate.count("R")
        banD=banR=0
        que=deque(senate)
        while(countR and countD):
            if(que[0]=="R"):
                if(banR>0):
                    countR-=1
                    banR-=1
                    que.popleft()
                else:
                    banD+=1
                    que.append(que.popleft())
            else:
                if(banD>0):
                    countD-=1
                    banD-=1
                    que.popleft()
                else:
                    banR+=1
                    que.append(que.popleft())
        if(countD>countR):
            return "Dire"
        return "Radiant"