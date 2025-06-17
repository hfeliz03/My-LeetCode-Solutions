class MinStack:

    def __init__(self):
        self.val = []
        self.min = []
        self.topVal = None

    def push(self, val: int) -> None:
        self.val.append(val)
        if not self.min or val <= self.min[-1]:
            self.min.append(val)
        self.topVal = val

    def pop(self) -> None:
        if self.val:
            popped = self.val.pop()
            if popped == self.min[-1] :
                self.min.pop()
            self.topVal = self.val[-1] if self.val else None
        

    def top(self) -> int:
        return self.topVal

    def getMin(self) -> int:
        return self.min[-1] if self.min else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()