class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = float("inf")

    def push(self, val: int) -> None:
        self.stack.append((val, self.min_val))
        if val < self.min_val:
            self.min_val = val

    def pop(self) -> None:
        val = self.stack.pop()
        self.min_val = val[1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min_val
