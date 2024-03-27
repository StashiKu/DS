class Node:
    def __init__(self, val, next = None, random = None):
        self.val = val
        self.next = next
        self.random = random


def solution(head):
    if (head is None):
        return



head = Node(0)
first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)

head.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = second
third.random = fifth
fourth.random = head
fifth.random = third


count = 1
target = 2

while next.next != curr:
    prev = curr
    if count == target:
        curr.next = None
        prev = None

    curr = next

    next = curr.next
    curr.next = prev

    count += 1
