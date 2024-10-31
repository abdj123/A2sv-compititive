# Problem: Arrays Subset Of Another Array - https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

#User function Template for python3
from collections import Counter

def isSubset( a1, a2, n, m):
    count = Counter(a1)
    
    for i in a2:
        if count[i] > 0:
            count[i] -= 1
        else:
            return "No"
    return "Yes"
    
    
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


        print("~")
if __name__ == "__main__":
    main()

# } Driver Code Ends