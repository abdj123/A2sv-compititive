# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        distances = [0] * n
        distances[0]=1
        for i in range(len(edges)):
            u,v = edges[i]
            prob = succProb[i]
            graph[u].append((v,prob))
            graph[v].append((u,prob))
        
        heap = [(-1,start_node)]

        while heap:
            prob, u = heappop(heap)
            for v,p in graph[u]:
                distance = prob * p
                if distances[v] > distance:
                    distances[v] = distance
                    heappush(heap,(distance,v))
        
        return 0 if distances[end_node] == 0 else -distances[end_node]


        
