class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        c = 0
        rows = len(mat)
        cols = len(mat[0])
        out = [[] for i in range(rows+cols-1)]

        for row in range(rows):
            for col in range(cols):
                out[c+col].append(mat[row][col])
            c+=1
        p = [out[i][::-1] if i%2==0 else out[i] for i in range(len(out))]
        x = []
        for i in p:
            x.extend(i)
        return x