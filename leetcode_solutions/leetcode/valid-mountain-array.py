class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i=1
        while(i<len(arr) and arr[i]>arr[i-1]):
            i+=1
        if(i==1 or i==len(arr)):
            return False
        while(i<len(arr) and arr[i]<arr[i-1]):
            i+=1
        return i==len(arr)
        