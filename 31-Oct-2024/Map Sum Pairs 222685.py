# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.sum = 0
        self.children = [None for _ in range(26)]


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.visit = {}

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        if key in self.visit:

            for c in key:
                indx = ord(c) - ord("a")
                if curr.children[indx] == None:
                    curr.children[indx] = TrieNode()
                prev = self.visit[key]
                curr.sum -= prev
                curr.sum += val
                curr = curr.children[indx]
            curr.sum -= self.visit[key]
            curr.sum += val
            self.visit[key] = val
        else:
            self.visit[key] = val
            for c in key:
                indx = ord(c) - ord("a")
                if curr.children[indx] == None:
                    curr.children[indx] = TrieNode()
                curr.sum += val
                curr = curr.children[indx]
            curr.sum += val

    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            indx = ord(c) - ord("a")
            if curr.children[indx] == None:
                return 0
            curr = curr.children[indx]
        return curr.sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
