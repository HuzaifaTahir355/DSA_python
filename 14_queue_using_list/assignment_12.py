class Queue:
    def __init__(self):
        self.list = []
        self.item_count = 0
        self.front_value = None
        self.rear_value = None

    def is_empty(self):
        return self.item_count == 0

    def enqueue(self, data):
        if self.is_empty():
            self.front_value = data
        else:
            self.rear_value = data
        self.list.append(data)
        self.item_count += 1

    def dequeue(self):
        if not self.is_empty():
            self.list.remove(self.front_value)
            self.item_count -= 1
            if self.is_empty():
                self.front_value = None
                self.rear_value = None
            else:
                self.front_value = self.list[0]

    def get_front(self):
        return self.front_value

    def get_rear(self):
        return self.rear_value

    def size(self):
        return self.item_count


# Testing
q1 = Queue()
# print(q1.is_empty())
# print(q1.size())
q1.enqueue(10)
q1.enqueue(20)
print(q1.get_front())
print(q1.get_rear())
print(q1.size())
q1.dequeue()
print(q1.get_front())
print(q1.get_rear())
q1.dequeue()
print(q1.size())
print(q1.get_front())
print(q1.get_rear())
print(q1.size())
