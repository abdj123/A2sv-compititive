class Node:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = Node(homepage)
        self.current = self.history

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.current.next = newNode
        newNode.prev = self.current
        self.current = self.current.next

    def back(self, steps: int) -> str:
        while self.current and self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1
        
        return self.current.val

    def forward(self, steps: int) -> str:
        while self.current and self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1
        
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)