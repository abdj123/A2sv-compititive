class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        arr=[]
        ans = []
        for i in s:
            if i == "*":
                arr.append(1)
            else:
                arr.append(0)
            
        prefix=[0]
        for i in range(len(arr)):
            prefix.append(prefix[-1]+arr[i])
        
        res = []
        for i in range(len(s)):
            if s[i] == '|':
                res.append(i)     
      
        for a,b in queries:
            if a == b:
                ans.append(0)
                continue
            ind = bisect_left(res,a)
            if ind< len(res):
                l =  res[ind]
                r = res[bisect_right(res,b)-1]
            else:
                ans.append(0)
                continue
            if l > r:
                ans.append(0)
                continue
            ans.append(prefix[r]-prefix[l])
        return ans
