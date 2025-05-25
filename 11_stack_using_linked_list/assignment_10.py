from SLL_code import SLL

class Stack:
    def __init__(self):
        self.list = SLL()
        self.item_count = 0

    def is_empty(self):
        return self.list.is_empty()

    def push(self, data):
        self.list.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            item_to_delete = self.list.start.item
            self.list.delete_first()
            self.item_count -= 1
            return item_to_delete

    def peek(self):
        if not self.is_empty():
            return self.list.start.item

    def size(self):
        return self.item_count


# Testing
s1 = Stack()
print(s1.is_empty())
s1.push(24)
s1.push(28)
s1.push(22)
print(s1.pop())
print(s1.peek())
print(s1.is_empty())
print(s1.size())

