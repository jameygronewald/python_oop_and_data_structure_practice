class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None

class LinkedList: 
    def __init__(self):
        self.start = None

    def traverse_list(self):
        if self.start is None:
            print(f"This linked list contains no nodes.")
            return
        else:
            node = self.start
            while node is not None:
                print(f"{node.data}")
                node = node.pointer

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.pointer = self.start
        self.start = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        node = self.start
        while node.pointer is not None:
            node = node.pointer
        node.pointer = new_node

    def insert_after_node(self, x, data):
        node = self.start
        print(node.pointer)
        while node is not None:
            if node.data == x:
                break
            node = node.pointer
        if node is None:
            print('Item does not exist in this list.')
        else: 
            new_node = Node(data)
            new_node.pointer = node.pointer
            node.pointer = new_node

    def insert_before_node(self, x, data):
        if self.start is None:
            print('List has no nodes.')
            return
        if x == self.start:
            new_node = Node(data)
            new_node.pointer = self.start
            self.start = new_node
            return
        node = self.start
        print(node.pointer)
        while node.pointer is not None:
            if node.pointer.data == x:
                break
            node = node.pointer
        if node.pointer is None:
            print('Item does not exist in this list.')
        else:
            new_node = Node(data)
            new_node.pointer = node.pointer
            node.pointer = new_node

    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.pointer = self.start
            self.start = new_node
        i = 1
        node = self.start
        while i < index - 1 and node is not None:
            node = node.pointer
            i += 1
        if node is None:
            print('Index is out of bounds.')
        else: 
            new_node = Node(data)
            new_node.pointer = node.pointer
            node.pointer = new_node

linked_list = LinkedList()


linked_list.insert_at_end(4)
linked_list.insert_at_end(9)
linked_list.insert_at_start(1)
linked_list.insert_at_start(0)
linked_list.insert_before_node(9, 8)
linked_list.insert_after_node(4, 5)
linked_list.insert_at_index(3, 2)
            
print(linked_list.traverse_list())