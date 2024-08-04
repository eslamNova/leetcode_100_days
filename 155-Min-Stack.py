class MinStack:

    def __init__(self):
        self.stack = []
        self.minis = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minis[-1] if self.minis else val)
        self.minis.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minis.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minis[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()