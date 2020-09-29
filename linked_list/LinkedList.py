from Node import Node

class LinkedList:
    def __init__(self):
        self.start = None

    def print_list(self):
        if self.start is None:
            print(f"This list is empty.")
        node = self.start
        while node is not None:
            print(f"{node.value}")
            node = node.pointer

    def get_node(self, index):
        node = self.start
        if node == None:
            print(f"This linked list is empty.")
            return
        for _ in range(index):
            node = node.pointer
        print(node.value)

    def prepend_node(self, value):
        new_node = Node(value)
        if self.start is not None:
            new_node.pointer = self.start
        self.start = new_node
        print(f"Added node to start with value of {new_node.value}.")

    def add_node(self, index, value):
        new_node = Node(value)
        node = self.start
        if node is None:
            self.start = new_node
        while node is not None:
            for _ in range(index):
                node = node.pointer
        print(node)


linked_list = LinkedList()

linked_list.print_list()

linked_list.prepend_node(10)

linked_list.get_node(0)

linked_list.print_list()