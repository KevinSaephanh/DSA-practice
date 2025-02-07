class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        # Determine which half we should search on
        # Starting from the beginning when index is in the latter half would be a waste of time
        if index < self.length / 2:
            # Traverse from beginning up to index to get node
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            # Traverse backwards from end down to index to get node
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop()

        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.prev = None
        temp.next = None

        self.length -= 1


my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(8)
my_doubly_linked_list.append(9)
my_doubly_linked_list.pop()
my_doubly_linked_list.prepend(1)
my_doubly_linked_list.pop_first()
print(f"Get Node: {my_doubly_linked_list.get(3)}")
print(f"Get Node: {my_doubly_linked_list.get(10)}")
my_doubly_linked_list.set_value(3, 20)
my_doubly_linked_list.insert(3, 15)
my_doubly_linked_list.remove(2)
my_doubly_linked_list.print_list()
