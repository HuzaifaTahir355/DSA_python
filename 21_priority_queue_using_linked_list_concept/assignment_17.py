class Node:
    def __init__(self, item, priority, next_ref=None):
        self.item = item
        self.priority = priority
        self.next = next_ref

class PriorityQueue:
    def __init__(self):
        self.front = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0

    def push(self, item, priority):
        n = Node(item, priority)
        temp = self.front
        if temp is None or temp.priority > priority:
            n.next = self.front
            self.front = n
        else:
            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count += 1



    def pop(self):
        if not self.is_empty():
            item_to_del = self.front.item
            self.front = self.front.next
            self.item_count -= 1
            return item_to_del
        else:
            raise IndexError("Priority Queue is empty")

    def size(self):
        return self.item_count


# Testing
pq1 = PriorityQueue()
pq1.push(10, 1)
pq1.push(10, 2)
pq1.push(11, 2)
pq1.push(100, 5)
pq1.push(5, 1)

while not pq1.is_empty():
    print(pq1.pop())