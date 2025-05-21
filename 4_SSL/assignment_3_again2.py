class Node:
    def __init__(self, item=None, next_ref=None):
        self.item = item
        self.next = next_ref

class SLL:
    def __init__(self):
        self.start = None

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, item_to_insert):
        n = Node(item=item_to_insert, next_ref=self.start)
        self.start = n

    def insert_at_last(self, item_to_insert):

        if self.is_empty():
            self.insert_at_start(item_to_insert)
        else:
            n = Node(item=item_to_insert)
            # loop to get last object reference
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n

    def search(self, item_to_find):
        temp = self.start
        while temp is not None:
            if temp.item == item_to_find:
                print(temp.item)
                break
            temp = temp.next
        return temp

    def insert_after(self, existing_item, new_item):
        ref_object = self.search(existing_item)
        if ref_object:
            n = Node(item=new_item, next_ref=ref_object.next)
            ref_object.next = n

    def show_all_elements(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next

    def delete_first(self):
        if not self.is_empty():
            self.start = self.start.next

    def delete_last(self):
        if self.is_empty():
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self, item_to_delete):
        if self.is_empty():
            pass
        elif self.start.next is None:
            if self.start.item == item_to_delete:
                self.start = None
        else:
            temp = self.start



    def __iter__(self):
        return Iterator(self.start)

class Iterator:
    def __init__(self, starting_ref):
        self.current = starting_ref

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            data = self.current.item
            self.current = self.current.next
            return data


