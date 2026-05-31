class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        print(self.stack)

    def pop(self) -> None:
        if len(self.stack) != 0:
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[len(self.stack)-1]
        return 0

    def getMin(self) -> int:
        if len(self.stack) != 0:
            print(min(self.stack))
            return min(self.stack)
        return 0
