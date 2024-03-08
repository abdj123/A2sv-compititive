class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons=persons
        self.times=times

        self.res=[]
        dct=defaultdict(int)
        prev=persons[0]
        for a in range(len(persons)):
            dct[persons[a]]+=1
            if dct[persons[a]] >= dct[prev]:
                prev = persons[a]
            self.persons[a]=prev

    def q(self, t: int) -> int:
        bisect=bisect_right(self.times,t)
        return self.persons[bisect-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)