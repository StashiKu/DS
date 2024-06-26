class Node:
   def __init__(self, data=None, next=None):
       self.data = data
       self.next = next

   def __str__(self):
       return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def delete_first(self):
        if self.head is None:
            return
        self.head = self.head.next

    def delete_last(self):
        if self.head is None or self.head.next is None:
            self.head = None
            return

        current_node = self.head
        prev_node = current_node

        while current_node.next is not None:
            prev_node = current_node
            current_node = current_node.next

        prev_node.next = None

    def get_length(self):
        length = 0
        current_node = self.head

        while current_node is not None:
            length += 1
            current_node = current_node.next

        return length

    def insert_by_index(self, value, index):
        if index == 0:
            self.add_first(value)
            return
        new_node = Node(value)
        node_number = 1
        current_node = self.head
        while current_node is not None:
            if index == node_number:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
            node_number += 1

    def delete_by_index(self, index):
        if index == 0:
            self.delete_first()
            return
        node_number = 0
        current_node = self.head
        previous_node = current_node
        while current_node is not None:
            if index == node_number:
                previous_node.next = current_node.next
                current_node.next = None
                return
            previous_node = current_node
            current_node = current_node.next
            node_number += 1

    def set_value_by_index(self, value, index):
        node_number = 0
        current_node = self.head
        while current_node is not None:
            if index == node_number:
                current_node.data = value
                return
            current_node = current_node.next
            node_number += 1
        return None
