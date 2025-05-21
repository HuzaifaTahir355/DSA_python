class Node:
    def __init__(self, item, next_ref=None):
        self.item = item
        self.next = next_ref

class CLL:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        return self.last is None

    def insert_at_start(self, item):
        n = Node(item=item)
        if self.is_empty():
            self.last = n
            n.next = n
        else:
            n.next = self.last.next
            self.last.next = n

    def insert_at_last(self, item):
        n = Node(item=item)
        if self.is_empty():
            self.last = n
            n.next = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n

    def search(self, item):
        if self.is_empty():
            return None
        else:
            temp = self.last.next
            while temp != self.last:
                if temp.item == item:
                    return temp
                temp = temp.next
            if temp.item == item:
                return temp
        return None

    def insert_after(self, existing_item, new_item):
        n = Node(item=new_item)
        prev_item = self.search(existing_item)
        if prev_item:
            if prev_item.next == self.last:
                self.last = n
            n.next = prev_item.next
            prev_item.next = n

    def display_all_items(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.item)
                temp = temp.next
            print(temp.item)

    def delete_first(self):
        if not self.is_empty():
            if self.last.next != self.last:
                self.last.next = self.last.next.next
            else:
                self.last = None

    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

    # TODO: Need to adjust delete_item and iterator
    def delete_item(self, item):
        if not self.is_empty():
            if self.last.next == self.last:
                if self.last.item == item:
                    self.last = None
            else:
                temp = self.last
                while temp.next != self.last:
                    if temp.next.item == item:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    def __iter__(self):
        if self.last is None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)


class CLLIterator:
    def __init__(self, current):
        self.current = current
        self.start = current

    def __next__(self):
        if self.current is not None:
            if self.current.next == self.start:
                raise StopIteration
            self.current = self.current.next
            return self.current.item
        raise StopIteration


# Testing
c1 = CLL()
print(c1.is_empty())
c1.insert_at_start(3)
c1.insert_at_start(2)
c1.insert_at_last(20)
c1.insert_at_last(30)
c1.insert_at_start(1)
c1.insert_after(2, 2.5)
print([item for item in c1])
# print(c1.search(20))
# c1.delete_first()
# c1.delete_last()
# c1.delete_last()
# c1.display_all_items()
