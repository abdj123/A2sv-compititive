class RandomizedSet:

    def __init__(self):
        self.nums=set()

    def insert(self, val: int) -> bool:
        if(val not in self.nums):
            self.nums.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if(val not in self.nums):
            return False
        else:
            self.nums.remove(val)
            return True

    def getRandom(self) -> int:
        return random.choice(list(self.nums))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()