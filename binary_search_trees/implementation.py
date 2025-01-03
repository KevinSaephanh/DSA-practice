class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return new_node

        # Find node that will be parent of new node
        # Move to appropriate subtree depending on value comparison
        # Higher curr value means new node will be on left, lower means right
        parent = None
        curr = self.root
        while curr:
            parent = curr
            if curr.value > value:
                curr = curr.left
            elif curr.value < value:
                curr = curr.right
            else:
                return self.root

        # If value is smaller, move to left; else right
        if parent.value > value:
            parent.left = new_node
        else:
            parent.right = new_node

        return new_node

    def contains(self, value):
        curr = self.root
        while curr:
            if curr.value > value:
                curr = curr.left
            elif curr.value < value:
                curr = curr.right
            else:
                return True
        return False


tree = BinarySearchTree(2)
tree.insert(3)
tree.insert(5)
tree.insert(13)
print(tree.contains(3))
print(tree.contains(4))
