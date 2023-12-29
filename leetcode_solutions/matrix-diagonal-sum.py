class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        sum_=0
        j=k=0
        
        for i in range(len(mat)):
            sum_+=mat[j][k]
            j+=1
            k+=1
        
        k,j=len(mat)-1,0
        
        for i in range(len(mat)):
            if(k!=j):
                sum_+=mat[k][j]
            j+=1
            k-=1
            
        return sum_
                