class Node:
    def __init__(self, item=None, next_ref=None):
        self.item = item
        self.next = next_ref

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        n = Node(data)
        self.item_count += 1
        if self.rear:
            self.rear.next = n
            self.rear = n
        else:
            self.front = n
            self.rear = n

    def dequeue(self):
        if not self.is_empty():
            self.front = self.front.next
            self.item_count -= 1
        else:
            raise IndexError("Queue is Empty")

    def get_front(self):
        if self.front:
            return self.front.item
        else:
            raise IndexError("Queue is Empty")

    def get_rear(self):
        if self.rear:
            return self.rear.item
        else:
            raise IndexError("Queue is Empty")

    def size(self):
        return self.item_count

# Testing
s1 = Queue()
# print(s1.get_front())
# print(s1.get_rear())
# print(s1.is_empty())
# s1.dequeue()
# print(s1.size())
s1.enqueue(10)
s1.enqueue(20)
s1.enqueue(30)
print("Size of the Queue is: ", s1.size())
print("First Element of Queue is: ", s1.get_front())
print("Last Element of Queue is: ", s1.get_rear())
print("==> Deleting First Element...")
s1.dequeue()
print("Size of the Queue is: ", s1.size())
print("First Element of Queue is: ", s1.get_front())
print("Last Element of Queue is: ", s1.get_rear())
print("==> Deleting First Element...")
s1.dequeue()
print("Size of the Queue is: ", s1.size())
print("First Element of Queue is: ", s1.get_front())
print("Last Element of Queue is: ", s1.get_rear())
# print("==> Deleting First Element...")
# s1.dequeue()
# print("Size of the Queue is: ", s1.size())
# print("First Element of Queue is: ", s1.get_front())
# print("Last Element of Queue is: ", s1.get_rear())
