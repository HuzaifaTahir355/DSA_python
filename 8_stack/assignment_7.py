class Stack:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return False if self.list else True

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if not self.is_empty():
            self.list.pop()

    def peek(self):
        if not self.is_empty():
            return self.list[-1]

    def size(self):
        return len(self.list)



# Testing
s1 = Stack()
print(s1.is_empty())
s1.push(1)
s1.push(2)
s1.push(5)
s1.push(8)
print(s1.is_empty())
s1.pop()
print(s1.peek())
print(s1.size())