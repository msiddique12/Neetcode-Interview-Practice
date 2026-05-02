class MinStack:

    def __init__(self):
        self.stack = []
        self.minValue = float('inf')

    def push(self, val: int) -> None:
        if val < self.minValue:
            self.minValue = val
        self.stack.append((val, self.minValue))

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.minValue = self.stack[-1][1]
        else:
            self.minValue = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minValue
