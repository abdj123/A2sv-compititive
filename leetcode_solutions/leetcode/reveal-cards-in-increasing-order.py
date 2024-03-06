class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        que=deque()
        for i in sorted(deck,reverse=True):
            if(que):
                que.appendleft(que.pop())
            que.appendleft(i)
        return list(que)
        