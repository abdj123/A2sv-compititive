class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            return min(sum(distance)-sum(distance[destination:start]), sum(distance[destination:start]))
        else:
            return min(sum(distance)-sum(distance[start:destination]), sum(distance[start:destination]))
        