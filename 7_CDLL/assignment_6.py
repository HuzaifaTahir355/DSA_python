class Node:
    def __init__(self, prev_ref=None, item=None, next_ref=None):
        self.prev = prev_ref
        self.item = item
        self.next = next_ref

class CDLL:
    def __init__(self):
        self.start = None

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(item=data)
        if self.is_empty():
            n.prev = n
            n.next = n
        else:
            n.prev = self.start.prev
            n.next = self.start
            self.start.prev.next = n
            self.start.prev = n
        self.start = n

    def insert_at_last(self, data):
        n = Node(item=data)
        if self.is_empty():
            n.prev = n
            n.next = n
            self.start = n
        else:
            n.prev = self.start.prev
            n.next = self.start
            self.start.prev.next = n
            self.start.prev = n

    def search(self, data):
        if self.is_empty():
            return None
        else:
            temp = self.start
            while temp.next != self.start:
                if temp.item == data:
                    return temp
                temp = temp.next
            if temp.item == data:
                return temp
            return None

    def insert_after(self, existing_data, new_data):
        n = Node(item=new_data)
        existing_node = self.search(existing_data)
        if existing_node:
            n.prev = existing_node
            n.next = existing_node.next
            existing_node.next.prev = n
            existing_node.next = n

    def print_all_elements(self):
        if not self.is_empty():
            temp = self.start
            while temp.next != self.start:
                print(temp.item)
                temp = temp.next
            print(temp.item)

    def delete_first(self):
        if not self.is_empty():
            if self.start.next != self.start:
                self.start.next.prev = self.start.prev
                self.start.prev.next = self.start.next
                self.start = self.start.next
            else:
                self.start = None

    def delete_last(self):
        if not self.is_empty():
            if self.start.next != self.start:
                self.start.prev.prev.next = self.start.prev.next
                self.start.prev = self.start.prev.prev
            else:
                self.start = None

    def delete_item(self, existing_data):
        if not self.is_empty():
            existing_node = self.search(existing_data)
            if existing_node:
                if existing_node.next == existing_node.prev:
                    self.start = None
                else:
                    existing_node.prev.next = existing_node.next
                    existing_node.next.prev = existing_node.prev
                    if existing_node == self.start:
                        self.start = self.start.next

# TODO: Iteration remaining




io1 = CDLL()
print(io1.is_empty())
# io1.insert_at_last(10)
io1.insert_at_start(5)
io1.insert_at_last(10)
io1.insert_after(5, 15)
print(io1.search(15))
io1.print_all_elements()
io1.delete_first()
io1.delete_last()
io1.delete_item(15)
# io1.delete_last()
io1.print_all_elements()
print(io1.is_empty())
# print(io1.search(5))
# print(io1.search(3))
