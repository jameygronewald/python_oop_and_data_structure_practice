from Node import Node

class LinkedList:
    def __init__(self):
        self.start = None

    def print_list(self):
        current_node = self.start
        if current_node is None:
            print(f"This list is empty.")
        index = 0
        while current_node is not None:
            print(f"Index {index}: {current_node.value}")
            index += 1
            current_node = current_node.next

    def get_node(self, index):
        current_node = self.start
        if current_node is None:
            print(f"This linked list is empty.")
            return
        for _ in range(index):
            current_node = current_node.next
        print(f"Node at position {index} is {current_node.value}.")

    def prepend_node(self, value):
        new_node = Node(value)
        if self.start is not None:
            new_node.next = self.start
        self.start = new_node
        print(f"Added a node to start of list with a value of {new_node.value}.")

    def append_node(self, value):
        new_node = Node(value)
        current_node = self.start
        if current_node is None:
            self.start = new_node
            return
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        print(f"Added a node to end of list with a value of {new_node.value}.")

    def insert_node(self, index, value):
        new_node = Node(value)
        current_node = self.start
        if current_node is None:
            print(f"This list is empty. Please add nodes in order to insert a node.")
            return
        if index == 0:
            self.prepend_node(value)
            return
        for _ in range(index - 1):
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
        print(f"Node inserted at index {index} with a value of {new_node.value}.")

    def delete_node_at_start(self):
        if self.start is None:
            print(f"This last has no nodes to delete.")
            return
        self.start = self.start.next
        print('First node in list was deleted.')

    def delete_node_at_end(self):
        current_node = self.start
        if current_node is None:
            print(f"This last has no nodes to delete.")
            return
        elif current_node.next is None:
            self.start = None
            print(f"Deleted node. Only one node was in list so list is now empty.")
            return
        while current_node.next.next is not None:
            current_node = current_node.next
        current_node.next = None
        print(f"Last node in list deleted.")

    def delete_node_at_index(self, index):
        current_node = self.start
        if current_node is None:
            print(f"This last has no nodes to delete.")
            return
        elif current_node.next is None:
            self.start = None
            print(f"Deleted node. Only one node was in list so list is now empty.")
            return
        for _ in range(index - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        print(f"Deleted node at index {index}.")

    def count_list(self):
        current_node = self.start
        if current_node is None:
            return print("List is empty.")
        else: count = 1
        while current_node.next is not None:
            current_node = current_node.next
            count += 1
        return print(f"The list is {count} nodes long.")

linked_list = LinkedList()
print('\n///count///')
linked_list.count_list()
print('\n///print///')
linked_list.print_list()
print('\n///prepend///')
linked_list.prepend_node(10)
print('\n///append///')
linked_list.append_node(12)
print('\n///prepend///')
linked_list.prepend_node(-5)
print('\n///insert///')
linked_list.insert_node(2, 4)
print('\n///insert///')
linked_list.insert_node(0, 1000)
print('\n///get [0]///')
linked_list.get_node(0)
print('\n///count///')
linked_list.count_list()
print('\n///print///')
linked_list.print_list()
print('\n///delete at start///')
linked_list.delete_node_at_start()
print('\n///delete at end///')
linked_list.delete_node_at_end()
print('\n///prepend///')
linked_list.prepend_node(3)
print('\n///prepend///')
linked_list.prepend_node(748)
print('\n///prepend///')
linked_list.prepend_node(64)
print('\n///delete at [4]///')
linked_list.delete_node_at_index(4)
print('\n///count///')
linked_list.count_list()
print('\n///print///')
linked_list.print_list()
