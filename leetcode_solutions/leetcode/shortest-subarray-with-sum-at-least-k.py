class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        B = [0] * (N + 1)
        for i in range(N): B[i + 1] = B[i] + nums[i]
        d = collections.deque()
        res = N + 1
        for i in range(N + 1):
            while d and B[i] - B[d[0]] >= k: res = min(res, i - d.popleft())
            while d and B[i] <= B[d[-1]]: d.pop()
            d.append(i)
        return res if res <= N else -1



