class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if validator(board):
            transpose=[]
            for i in range(9):
                tmp=[]
                for j in range(9):
                    tmp.append(board[j][i])
                transpose.append(tmp)
            if validator(transpose):
                for k in range(9):
                    for j in range(9):

                        tmp=[row[j*3:(j+1)*3] for row in board[k*3:(k+1)*3]]
                        if(len(tmp)>1 and tmp[0]!=[]):
                            temp=[item for sublist in tmp for item in sublist]
                            count=Counter(temp)
                            print(temp)
                            for ke,v in count.items():
                                if(ke!="." and v>1):
                                    return False
                                
            else:
                return False
        else:
            return False
                
                    
        return True
def validator(board):
        
        for i in board:
            count=Counter(i)
            for k,v in count.items():
                if(k!="." and v>1):
                    return False
        return True

    
        