class Node:
    def __init__(self, item=None, next_ref=None):
        self.item = item
        self.next = next_ref
    
class SLL:
    def __init__(self, start=None):
        self.start = start
    
    def is_empty(self):
        return self.start == None

    def insert_at_start(self, item_to_insert):
        n = Node(item=item_to_insert, next_ref=self.start)
        self.start = n

    def insert_at_last(self, item_to_insert):
        if self.is_empty():
            self.insert_at_start(item_to_insert) # we also can simply assign n to self.start but need to create node outside.
        else:
            n = Node(item=item_to_insert)
            # loop to get last object reference
            temp = self.start
            while(temp.next is not None):
                temp = temp.next
            temp.next = n
    
    def search(self, item_to_find):
        temp = self.start
        while(temp is not None):
            if temp.item == item_to_find:
                print(temp.item) # cross check
                break
            temp = temp.next
        return temp
    
    def insert_after(self, existing_item, new_item):
        existing_node = self.search(existing_item)
        if existing_node:
            print(f"Item -> {existing_node.item}\nNode reference -> {existing_node}")
            # create new node
            n = Node(item=new_item, next_ref=existing_node.next)
            existing_node.next = n
            return "Added Successfully"
        else:
            return "Existing Item Not Found"

    def show_all_elements(self):
        temp = self.start
        while(temp is not None):
            print(temp.item, end=" ")
            temp = temp.next
    
    def delete_first(self):
        if not self.is_empty():
            self.start = self.start.next

    def delete_last(self):
        if self.is_empty():
            return "List is Empty"
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while(temp.next.next is not None):
                temp = temp.next
            temp.next = None
                
    def delete_item(self, item_to_del):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == item_to_del:
                self.start = None
        else:
            temp = self.start
            if temp.item == item_to_del:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == item_to_del:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
    
    # to make you class iterable, you need to override a function named __iter__
    # and need to return the object of iterator class
    def __iter__(self):
        return SLLIterator(self.start)


class SLLIterator:
    # Every class is the child class of object class in python
    # Object class contain some important attributes i.e __init__, __iter__, __next__ etc
    # How to check the methods and parent classes of your class. please read notes.txt -> (1)
    def __init__(self, start):
        self.current = start


    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

