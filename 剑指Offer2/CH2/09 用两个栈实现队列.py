class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        if not self.stack1:
            return -1
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

################### Test ########################
queue = CQueue()
queue.appendTail(1)
queue.appendTail(2)
a = queue.deleteHead()
print(a)
b = queue.deleteHead()
print(b)
c = queue.deleteHead()
print(c)