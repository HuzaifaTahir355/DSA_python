class Node:
    def __init__(self, item, left=None, right=None):
        self.left = left
        self.item = item
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, ref_node, data):
        if self.is_empty():
            self.root = Node(item=data)
        else:
            if data > ref_node.item:
                if ref_node.right is None:
                    ref_node.right = Node(item=data)
                else:
                    self.insert(ref_node.right, data)
            elif data < ref_node.item:
                if ref_node.left is None:
                    ref_node.left = Node(item=data)
                else:
                    self.insert(ref_node.left, data)
            else:
                raise AssertionError(f"{data} is already exist!")

    def search(self, data):
        temp = self.root
        while temp is not None:
            if temp.item == data:
                return temp
            elif data < temp.item:
                temp = temp.left
            else:
                temp = temp.right

    def preorder_traversing(self, ref_node):
        print(ref_node.item)
        if ref_node.left is not None:
            self.preorder_traversing(ref_node.left)
        if ref_node.right is not None:
            self.preorder_traversing(ref_node.right)

    def inorder_traversing(self, ref_node):
        if ref_node.left is not None:
            self.inorder_traversing(ref_node.left)
        print(ref_node.item)
        if ref_node.right is not None:
            self.inorder_traversing(ref_node.right)

    def postorder_traversing(self, ref_node):
        if ref_node.left is not None:
            self.postorder_traversing(ref_node.left)
        if ref_node.right is not None:
            self.postorder_traversing(ref_node.right)
        print(ref_node.item)

    def __remove_item_having_two_children(self, pointer):
        prnt_temp = pointer
        temp = prnt_temp.left
        while temp.right is not None:
            prnt_temp = temp
            temp = temp.right
        pointer.item = temp.item
        self.__delete_an_item(prnt_temp, temp)

    def __delete_an_item(self, parent_pointer, pointer):
        if parent_pointer != pointer:                                   # to confirm that this is not a root node
            direction = "right"
            if parent_pointer.left is not None and parent_pointer.left.item == pointer.item:
                direction = "left"

            if pointer.left is None and pointer.right is None:          # No child
                setattr(parent_pointer, direction, None)
            elif pointer.left is not None and pointer.right is None:    # Single left child
                setattr(parent_pointer, direction, pointer.left)
            elif pointer.right is not None and pointer.left is None:    # Single right child
                setattr(parent_pointer, direction, pointer.right)
            else:                                                       # Two children
                self.__remove_item_having_two_children(pointer)
        else:
            self.__remove_item_having_two_children(pointer)


    def delete(self, data, parent_pointer, pointer):
        if self.is_empty():
            raise IndexError("Tree is Empty")
        else:
            if pointer.item == data:
                return self.__delete_an_item(parent_pointer, pointer)
            elif data < pointer.item:
                if pointer.left is not None:
                    self.delete(data, pointer, pointer.left)
                else:
                    raise ValueError(f"{data} not Found in the Tree (left)!")
            else:
                if pointer.right is not None:
                    self.delete(data, pointer, pointer.right)
                else:
                    raise ValueError(f"{data} not Found in the Tree (right)!")


    def get_min_value(self):
        if self.is_empty():
            raise IndexError("Tree is Empty")
        else:
            temp = self.root
            while temp.left is not None and temp.right is not None:
                temp = temp.left
            return temp.item

    def get_max_value(self):
        if self.is_empty():
            raise IndexError("Tree is Empty")
        else:
            temp = self.root
            while temp.left is not None and temp.right is not None:
                temp = temp.right
            return temp.item



# Testing
bst = BST()

# items_to_insert = [50, 30, 80, 10, 40]
items_to_insert = [50, 30, 80, 10, 40, 70, 100, 35, 60, 75, 90, 55, 57]
for item in items_to_insert:
    bst.insert(bst.root, item)

# bst.preorder_traversing(bst.root)
# bst.inorder_traversing(bst.root)
# bst.postorder_traversing(bst.root)

# print(f"+++++++++++++++ deleting item +++++++++++++++")
# bst.delete(50, bst.root, bst.root)
# bst.inorder_traversing(bst.root)

print(bst.get_min_value())
print(bst.get_max_value())