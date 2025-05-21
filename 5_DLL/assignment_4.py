class Node:
    def __init__(self, item, prev_ref=None, next_ref=None):
        self.prev = prev_ref
        self.item = item
        self.next = next_ref

class DLL:
    def __init__(self):
        self.start = None

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, item_to_insert):
        n = Node(item=item_to_insert, next_ref=self.start)
        if not self.is_empty():
            n.next.prev = n
        self.start = n

    def insert_at_last(self, item_to_insert):
        if self.is_empty():
            self.insert_at_start(item_to_insert)
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(prev_ref=temp, item=item_to_insert)

    def search(self, item_to_search):
        if self.is_empty():
            return None
        elif self.start.item == item_to_search:
            return self.start
        else:
            temp = self.start
            while temp.next is not None:
                if temp.next.item == item_to_search:
                    return temp.next
                temp = temp.next
            return None

    def insert_after(self, previous, new):
        element_object = self.search(previous)
        if element_object:
            n = Node(prev_ref=element_object, item=new, next_ref=element_object.next)
            element_object.next = n
        else:
            return element_object

    def display_all_elements(self):
        if not self.is_empty():
            print(self.start.item)
            temp = self.start
            while temp.next is not None:
                print(temp.next.item)
                temp = temp.next

    def delete_first(self):
        if not self.is_empty():
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        if self.is_empty():
            return None
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self, item_to_del):
        element_object = self.search(item_to_del)
        if element_object:
            if element_object.prev is not None:
                element_object.prev.next = element_object.next
                if element_object.next is not None:
                    element_object.next.prev = element_object.prev
            else:
                self.delete_first()

    def __iter__(self):
        return DLLIterator(self.start)



class DLLIterator:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

# ============================ Testing
dll1 = DLL()
dll1.insert_at_start(5)
dll1.insert_at_start(3)
dll1.insert_at_start(1)
dll1.insert_at_last(7)
dll1.insert_after(7, 9)
dll1.display_all_elements()
[print(i, end=" ") for i in dll1]
# dll1.delete_first()
# dll1.delete_last()
# dll1.delete_item(9)
print("")
[print(i, end=" ") for i in dll1]
[dll1.delete_item(i) for i in dll1]
print(dll1.is_empty())
# [dll1.delete_item(i) for i in dll1]
