# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        left = 0
        right = row*col-1
        while left<=right:
            mid = left + (right-left)//2

            i = mid//col
            j = mid%col

            if matrix[i][j] < target:
                left = mid +1
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                return True
        return False
            
        