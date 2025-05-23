class Stack(list):
    def is_empty(self):
        return False if self else True

    def push(self, data):
        self.append(data)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty")

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")

    def size(self):
        return len(self)

    def insert(self, index, data):
        raise AttributeError("Insert is not supported in Stack")


# Testing
s1 = Stack()