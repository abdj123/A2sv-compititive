class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        while len(arr)>1:
            mx = max(arr)
            i = arr.index(mx)
            if i == 0:
                res.append(len(arr))
                arr = arr[1::][::-1]
                continue
            if i != len(arr)-1:
                res.append(i+1)
                arr = arr[:i+1][::-1]+arr[i+1:]
                res.append(len(arr))
                arr = arr[1::][::-1]
            else:
                arr = arr[:-1]
        return res
        