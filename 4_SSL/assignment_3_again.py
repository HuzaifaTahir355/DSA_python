class Node:
    def __init__(self, item=None, next_ref=None):
        self.item = item
        self.next = next_ref

class SLL:
    def __init__(self):
        self.start = None

    def is_empty(self):
        # if not self.start:
        #     return True
        # else:
        #     return False
        # return False if self.start else True
        return self.start == None

    def insert_at_start(self, item):
        new_node = Node(item=item, next_ref=self.start)
        # new_node.item = item
        # new_node.next = self.start
        self.start = new_node

    def insert_at_last(self, item):
        new_node = Node(item=item, next_ref=None)
        if self.start == None:
            self.start = new_node
        else:
            temp_var = self.start
            # while temp_var.next != None:
            while (temp_var.next is not None):
                temp_var = temp_var.next
            temp_var.next = new_node

    def search(self, item_to_search):
        if self.is_empty():
            return None
        else:
            temp_var = self.start
            while (temp_var is not None):
                if temp_var.item == item_to_search:
                    return temp_var.item
                temp_var = temp_var.next
            return None
        
    def insert_after(self, existing_item, new_item):
        new_node = Node(item=new_item)
        if self.is_empty():
            self.start = new_node
            return "Added Successfully"
        else:
            temp_var = self.start
            while (temp_var is not None):
                if temp_var.item == existing_item:
                    new_node.next = temp_var.next
                    temp_var.next = new_node
                    return "Added Successfully"
                temp_var = temp_var.next
            return "Existing Item Not Found"

    def show_all_elements(self):
        if self.is_empty():
            return "List is empty"
        else:
            temp_var = self.start
            while(temp_var is not None):
                print(temp_var.item)
                temp_var = temp_var.next
    
    def delete_first(self):
        if self.is_empty():
            return "List is empty"
        else:
            self.start = self.start.next

    def delete_last(self):
        if self.is_empty():
            return "List is empty"
        elif self.start.next is None:
            self.start = None
        else:
            temp_var = self.start
            while (temp_var.next.next is not None):
                temp_var = temp_var.next
            temp_var.next = None
            return "Item deleted successfully"
            
    def delete_item(self, item_to_delete):
        if self.is_empty():
            return "List is empty"
        elif self.start.next is None:
            if self.start.item == item_to_delete:
                self.start = self.start.next
        else:
            temp_var = self.start
            if temp_var.item == item_to_delete:
                self.start = self.start.next
            else:
                while temp_var.next is not None:
                    if temp_var.next.item == item_to_delete:
                        temp_var.next = temp_var.next.next
                        break
                    temp_var = temp_var.next

    def __iter__(self):
        return Iterator(self.start)


class Iterator:
    def __init__(self, start_reference):
        self.current = start_reference
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data




o1 = SLL()
# print(o1.is_empty())
o1.insert_at_start(5)
o1.insert_at_last(10)
o1.insert_at_last(11)
# print(o1.is_empty())
print(o1.insert_after(5, 7))
# o1.show_all_elements()
# print(o1.delete_item(5))
# o1.show_all_elements()
print(o1.search(7))