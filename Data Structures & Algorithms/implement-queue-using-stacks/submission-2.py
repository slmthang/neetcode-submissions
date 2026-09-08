class MyQueue:

    def __init__(self):
        self.out_arr = []
        self.in_arr = []        

    def push(self, x: int) -> None:
        self.in_arr.append(x) # 1, 2, 3, 4

    def pop(self) -> int:

        if not self.out_arr:
            while self.in_arr:
                self.out_arr.append(self.in_arr.pop())
        
        return self.out_arr.pop()

    def peek(self) -> int:

        if not self.out_arr:
            while self.in_arr:
                self.out_arr.append(self.in_arr.pop())
        
        return self.out_arr[-1]

    def empty(self) -> bool:
        
        return not self.out_arr and not self.in_arr