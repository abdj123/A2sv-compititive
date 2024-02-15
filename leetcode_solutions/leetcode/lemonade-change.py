class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives=0
        tens=0
        for i in range(len(bills)):
            
            if(bills[i]==5):
                fives+=1
            elif(bills[i]==10):
                
                tens+=1
                fives-=1
            elif(tens>0):
                
                tens-=1
                fives-=1
            else:
                fives-=3
            if(fives<0):
                return False
            
        return True