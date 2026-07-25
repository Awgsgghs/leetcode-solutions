class MinStack:
    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minstack or value<=self.minstack[-1]:
            self.minstack.append(value)

    def pop(self) -> None:
        if self.stack.pop()==self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
