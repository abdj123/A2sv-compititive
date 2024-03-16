class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        max_radius=0
        for i in range(len(houses)):
            index=bisect.bisect_left(heaters,houses[i])
            if index==0:
                max_radius=max(max_radius,abs(heaters[index]-houses[i]))
            if index>=len(heaters):
                max_radius=max(max_radius,abs(heaters[-1]-houses[i]))
            else:
                temp=min(abs(heaters[index]-houses[i]),abs(heaters[index-1]-houses[i]))
                max_radius=max(max_radius,temp)
        return max_radius
