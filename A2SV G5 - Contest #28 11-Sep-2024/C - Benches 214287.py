# Problem: C - Benches - https://codeforces.com/gym/540354/problem/C

import sys
from heapq import heapify, heappop, heappush
input = lambda: sys.stdin.readline().rstrip()


n = int(input())
m = int(input())
a = [int(input()) for line in range(n)]

_max = max(a) + m

heapify(a)
for i in range(m):
    min_bench = heappop(a)
    heappush(a, min_bench + 1)

_min = max(a)
print(_min, _max)