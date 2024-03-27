class Node:
    def __int__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)

class QueueDoublyLinkedList:
    def __int__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def add(self, value):
        new_node = Node(value, self.head.next, self.head)
        self.head.next = new_node
        new_node.next.prev = new_node
        self.length += 1

    def get_first(self):
        if self.is_empty():
            return
        return self.tail.prev

    def dequeue(self):
        if self.is_empty():
            return

        remove_node = self.tail.prev
        return_value = remove_node.data
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.prev.next = self.tail
        remove_node.next = None
        remove_node.prev = None
        self.length -= 1

        return return_value

    def is_empty(self):
        if self.head.next == self.tail:
            return True

        return False

    def get_length(self):
        if self.is_empty():
            return 0

        current_node = self.head.next
