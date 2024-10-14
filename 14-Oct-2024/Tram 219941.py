# Problem: Tram - https://codeforces.com/problemset/problem/116/A

n = int(input())
res = 0
curr = 0
for _ in range(n):
    a, b = map(int, input().split())
    curr -= a
    curr += b
    res = max(res, curr)
print(res)