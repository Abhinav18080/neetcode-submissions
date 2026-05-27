class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        result = self.stack.pop()
        self.stack.append(result)
        return result

    def getMin(self) -> int:
        return min(self.stack)
