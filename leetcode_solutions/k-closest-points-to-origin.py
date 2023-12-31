import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        temp=[]
        for x, y in points:
            temp.append([x**2+y**2, x, y])      
        temp.sort()
        output = []
        for i in range(k):
            
            output.append([temp[i][1],temp[i][2]])
            
        return output 
            
            