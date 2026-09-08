class MyStack:

    def __init__(self):
        self.arr1 = []
        self.arr2 = []

    def push(self, x: int) -> None:
        self.arr1.append(x)

        while self.arr2:
            self.arr1.append(self.arr2.pop(0))
        
        self.arr2 = self.arr1
        self.arr1 = []

    def pop(self) -> int:
        
        return self.arr2.pop(0)

    def top(self) -> int:
        return self.arr2[0]

    def empty(self) -> bool:
        return True if len(self.arr2) <= 0 else False