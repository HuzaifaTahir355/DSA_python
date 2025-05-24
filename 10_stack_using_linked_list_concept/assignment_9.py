class Node:
    def __init__(self, item, next_ref=None):
        self.item = item
        self.next = next_ref

class Stack:
    def __init__(self):
        self.start = None
        self.item_count =  0

    def is_empty(self):
        return self.item_count == 0

    def push(self, data):
        n = Node(data, self.start)
        self.start = n
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            item_to_delete = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return item_to_delete

    def peek(self):
        if not self.is_empty():
            return self.start.item

    def size(self):
        return self.item_count

# Testing
s1 = Stack()
print(s1.is_empty())
s1.push(50)
s1.push(60)
print(s1.size())
print(s1.peek())
print(s1.pop())
print(s1.pop())
print(s1.size())
s1.push(70)
print(s1.peek())
