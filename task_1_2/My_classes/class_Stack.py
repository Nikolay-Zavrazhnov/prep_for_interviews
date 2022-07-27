
# Задача 1
class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self) -> bool:
        if len(self.stack) == 0:
            return False
        else:
            return True

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty() is True:
            deleted = self.stack.pop()
            return deleted
        else:
            return 'stack is empty'

    def peek(self):
        if self.isEmpty() is True:
            return self.stack[-1]
        else:
            return 'stack is empty'

    def size(self):
        return len(self.stack)