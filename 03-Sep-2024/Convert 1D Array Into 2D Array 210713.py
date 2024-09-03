# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n*m != len(original):
            return []

        matrix = []
        temp = []

        for i in range(len(original)):
            temp.append(original[i])
            
            if len(temp) == n:
                matrix.append(temp)
                temp = []
        
        return matrix