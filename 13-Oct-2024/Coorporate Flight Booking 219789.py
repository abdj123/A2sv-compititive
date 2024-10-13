# Problem: Coorporate Flight Booking - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n + 1)

        for f, l, s in bookings:
            prefix[f - 1] += s
            prefix[l] -= s

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        return prefix[:-1]
