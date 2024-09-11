# Problem: D - Mr. Kitayuta's Colorful Graph - https://codeforces.com/gym/540354/problem/D

from sys import stdin
from collections import defaultdict


def input(): return stdin.readline().strip()

N, M = map(int, input().split())

graph = [defaultdict(list)  for _ in range(M)]

for _ in range(M):
    u, v, c = map(int, input().split())
    adj = graph[c - 1]
    adj[u].append(v)
    adj[v].append(u)

dest = -1
def dfs(v, adj, visited):
    visited.add(v)
    if v == dest:
        return True
    for u in adj[v]:
        if u not in visited:
            if dfs(u, adj, visited):
                return True
    return False


Q = int(input())
for _ in range(Q):
    cnt = 0
    u, v = map(int, input().split())
    for adj in graph:
        visited = set()
        dest = v
        if dfs(u, adj, visited):
            cnt += 1
    print(cnt)