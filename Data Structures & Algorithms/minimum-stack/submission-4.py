class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min = float('inf')

    def push(self, value: int) -> None:
        
        if value <= self.min:
            self.min = value
        self.min_stack.append(self.min)
        self.stack.append(value)

    def pop(self) -> None:
        popped = self.stack.pop()
        self.min_stack.pop()
        if self.min_stack:
            self.min = self.min_stack[-1]   
        else:
            self.min = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min