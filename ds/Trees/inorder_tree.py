class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class Inorder_Tree:
    # def __init__(self, root):
    #     self.root = root

    def in_order_traversal(self, node):
        if node == None:
            return

        # print(node.val, end=" ")
        self.in_order_traversal(node.left)

        # print(node.val, end=" ")

        self.in_order_traversal(node.right)
        print(node.val, end=" ")


root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.left.left.left = Node('F')
root.left.left.right = Node('G')
root.left.right.left = Node('H')
root.left.right.right = Node('I')
root.right.left = Node('J')
root.right.right = Node('K')
# root.right.left.left = Node('H')
# root.right.left.left = Node('I')
tree = Inorder_Tree()
print(tree.in_order_traversal(root))
