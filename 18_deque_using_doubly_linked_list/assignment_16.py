class Node:
    def __init__(self, prev=None, item=None, next_ref=None):
        self.prev = prev
        self.item = item
        self.next = next_ref

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.front is None

    def insert_front(self, data):
        n = Node(item=data, next_ref=self.front)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prev = n
        self.front = n
        self.item_count += 1

    def insert_rear(self, data):
        n = Node(prev=self.rear, item=data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1

    def delete_front(self):
        if not self.is_empty():
            if self.front == self.rear:
                self.front = self.rear = None
            else:
                self.front.next.prev = None
                self.front = self.front.next
            self.item_count -= 1

    def delete_rear(self):
        if not self.is_empty():
            if self.front == self.rear:
                self.front = self.rear = None
            else:
                self.rear.prev.next = None
                self.rear = self.rear.prev
            self.item_count -= 1

    def get_front(self):
        if not self.is_empty():
            return self.front.item

    def get_rear(self):
        if not self.is_empty():
            return self.rear.item

    def size(self):
        return self.item_count


# Testing
d1 = Deque()

d1.insert_front(10)
d1.insert_rear(20)
d1.insert_front(5)
d1.insert_rear(25)
d1.delete_front()
d1.delete_rear()
d1.delete_front()
d1.delete_rear()
print(d1.get_front())
print(d1.get_rear())
print(d1.size())