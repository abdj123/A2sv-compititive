# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        graph = defaultdict(list)
        visit = set()
        res = [""] * n

        for x, y in pairs:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):
            visit.add(node)
            indx.append(node)
            chars.append(s[node])
            for neb in graph[node]:
                if neb not in visit:
                    dfs(neb)

        for i in range(n):
            if i not in visit:
                indx = []
                chars = []
                dfs(i)

                indx.sort()
                chars.sort()

                for j in range(len(indx)):
                    res[indx[j]] = chars[j]

        return "".join(res)
