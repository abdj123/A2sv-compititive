class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        k = len(board[0])
        ln = len(word)
        def backtrack(row,col,index,path):
            #this is the base 
            if len(path)>ln or index >= ln:
                return True
            if( (row==n or row<0) or( col==k or col<0)) or ((row,col) in path) or ( board[row][col]!=word[index]):
                return
          
            # this is the recurence rel``at/ion
            path.add((row,col))
            rec = [(0,1),(0,-1),(1,0),(-1,0)]

            for r in rec:
                ans  = backtrack(row+r[0],col+r[1],index+1,path)   
                if ans:
                    return ans
            path.remove((row,col))


        n=len(board)
        m=len(board[0])
        for i in range(n):
            for j in range(m):
                if(backtrack(i,j,0,set())):
                    return True
        return False
