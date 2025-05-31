class PriorityQueue:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def push(self, item, priority):
        data = (item, priority)
        index = 0
        length_of_list = self.size()
        while index < length_of_list and self.list[index][1] <= priority:
            index += 1
        self.list.insert(index, data)

    def pop(self):
        if not self.is_empty():
            return self.list.pop(0)
        else:
            raise IndexError("Priority Queue is empty")

    def size(self):
        return len(self.list)

    def display_list(self):
        return self.list


# Testing
pq1 = PriorityQueue()
pq1.push(10, 1)
pq1.push(10, 2)
pq1.push(11, 2)
pq1.push(100, 50)
pq1.push(5, 1)
print(pq1.display_list())