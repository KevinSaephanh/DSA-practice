class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_pos(self, pos, value):
        if pos <= 0:
            self.insert_at_head(value)
            return

        new_node = Node(value)
        curr = self.head
        curr_pos = 0
        while curr and curr_pos < pos - 1:
            curr = curr.next
            curr_pos += 1

        if not curr:
            return "Invalid position"
        # Set new node's next pointer to curr's next then set curr's next to new node
        # Ex: 1 --> 2 --> curr --> curr.next ==> 1 --> 2 --> curr --> new_node --> curr.next
        new_node.next = curr.next
        curr.next = new_node

    def remove_at_head(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def remove_at_tail(self):
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next
        curr.next = None
        self.tail = curr

    def remove_node(self, value):
        curr = self.head
        prev = None
        while curr is not None:
            if curr.value == value:
                if prev is not None:
                    prev.next = curr.next
                    if curr.next is None:
                        self.tail = prev
                else:
                    self.remove_at_head()
                return True
            prev = curr
            curr = curr.next
        return False

    def find(self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    def set_value(self, old_value, new_value):
        curr = self.head
        while curr is not None:
            if curr.value == old_value:
                curr.value = new_value
                return True
        return False

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.value)
            curr = curr.next

    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            # Create temp
            next_node = curr.next
            # Reverse current node's next pointer to prev (1 --> 2 ==> 1 <-- 2)
            curr.next = prev
            # Increment pointers
            prev = curr
            curr = next_node
        # Swap head and tail
        self.head, self.tail = self.tail, self.head

    def empty_list(self):
        self.head = None
        self.tail = None


my_linked_list = LinkedList(1)
my_linked_list.insert_at_head(2)
my_linked_list.insert_at_head(3)
my_linked_list.insert_at_tail(4)
my_linked_list.insert_at_tail(5)
my_linked_list.insert_at_head(6)

my_linked_list.remove_at_head()
my_linked_list.print_list()

my_linked_list.reverse()
print("REVERSED")
my_linked_list.print_list()
