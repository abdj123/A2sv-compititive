# Problem: A - Memory and Crow - https://codeforces.com/gym/543431/problem/A

n = int(input())
ls = [int(i) for i in input().split()]

res = [ls[-1]]
ls.reverse()

for i in range(1,n):
    res.append(ls[i] + ls[i-1])

print(*res[::-1])