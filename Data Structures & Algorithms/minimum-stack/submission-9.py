class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_count = []
        self.current_value = 0
        self.lesser_value = 0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.current_value = val
        if len(self.minimum_count) == 0:
            self.lesser_value = val
        if self.current_value < self.lesser_value:
            self.lesser_value = val
        self.minimum_count.append(self.lesser_value)
        # return self.stack, self.minimum_count
        

    def pop(self) -> None:
        self.stack.pop()
        self.minimum_count.pop()
        #set cindition here for empty stack
        if len(self.minimum_count) != 0:
            self.lesser_value = self.minimum_count[-1]
        # return self.stack, self.minimum_count

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum_count[-1]
