class Deque:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def insert_front(self, data):
        self.list.insert(0, data)

    def insert_rear(self, data):
        self.list.append(data)

    def delete_front(self):
        if not self.is_empty():
            # item_to_del = self.get_front()
            # self.list.remove(item_to_del)
            # return item_to_del
            return self.list.pop(0)

    def delete_rear(self):
        if not self.is_empty():
            return self.list.pop()

    def get_front(self):
        if not self.is_empty():
            return self.list[0]

    def get_rear(self):
        if not self.is_empty():
            return self.list[-1]

    def size(self):
        return len(self.list)


