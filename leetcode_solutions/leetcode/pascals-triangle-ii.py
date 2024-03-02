class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def recur(n):
            if n == 0:
                return [1]
            if n == 1:
                return [1,1]
            row = self.getRow(n-1)
            ans = [1]
            for i in range(len(row)-1):
                ans.append(row[i]+row[i+1])
            ans.append(1)
            return ans
        return recur(rowIndex)