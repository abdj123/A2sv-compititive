class Bitset:

    def __init__(self, size: int):
        self.bitset = [0] * size
        self.size = size
        self.ones = 0
        self.flipped = False
        
		
    def fix(self, idx: int) -> None:
        if self.flipped and self.bitset[idx]:
            self.bitset[idx] = 0
            self.ones += 1
			
        elif not self.flipped and not self.bitset[idx]:
            self.bitset[idx] = 1
            self.ones += 1
        
		
    def unfix(self, idx: int) -> None:
        if self.flipped and not self.bitset[idx]:
            self.bitset[idx] = 1
            self.ones -= 1
			
        elif not self.flipped and self.bitset[idx]:
            self.bitset[idx] = 0
            self.ones -= 1
        
		
    def flip(self) -> None:
        self.flipped = not self.flipped
        self.ones = self.size - self.ones


    def all(self) -> bool:
        return self.ones == self.size
        

    def one(self) -> bool:
        return self.ones > 0
        
		
    def count(self) -> int:
        return self.ones
        
		
    def toString(self) -> str:
        if self.flipped:
            return "".join("0" if i else "1" for i in self.bitset)
        
        return "".join("1" if i else "0" for i in self.bitset)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()