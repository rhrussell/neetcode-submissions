class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        val= min(val, self.minStack[-1] if self.minStack else val)
        # this is the equivalent of this block of code
        # if self.minStack:
        #   previous_min = self.minStack[-1]
        # else:
        #   previous_min = val
        # val = min(val, previous_min)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        