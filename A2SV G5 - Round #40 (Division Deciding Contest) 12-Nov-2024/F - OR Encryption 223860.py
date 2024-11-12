# Problem: F - OR Encryption - https://codeforces.com/gym/543431/problem/F

import sys


def solve():
    n = int(sys.stdin.readline().strip())
    matrix = []

    for _ in range(n):
        row = list(map(int, sys.stdin.readline().strip().split()))
        matrix.append(row)

    a = [2**30 - 1] * n
    
    for i in range(n):
        for j in range(n):
            if i != j:
                a[i] &= matrix[i][j]
                a[j] &= matrix[i][j]

    for i in range(n):
        for j in range(n):
            if i != j and a[i] | a[j] != matrix[i][j]:
                print("NO")
                return
            
    print("YES")
    print(*a)
    
t = int(sys.stdin.readline().strip())

for _ in range(t):
    solve()