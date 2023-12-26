class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        bad = set()
        for a, b in zip(fronts, backs):
            if a == b:
                bad.add(a)
        res = float('inf')
        for a, b in zip(fronts, backs):
            if a not in bad:
                res = min(res, a)
            if b not in bad:
                res = min(res, b)
        return res if res != float('inf') else 0