# Partition a linked list such that all nodes with values less than x come before
# nodes with values greater than or equal to x
# Example:
#   Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1
#   x: 5
#   3 -> 2 -> 1 -> 8 -> 5 -> 10
from linked_lists.implementation import Node


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.length = 0


def partition_list(linked_list, x):
    # Create two dummy nodes for the two partitions
    before_head, after_head = Node(0), Node(0)
    # Pointers to traverse and build the partitions
    before = before_head
    after = after_head

    curr = linked_list.head
    while curr:
        if curr.value < x:
            # Point before's next pointer to curr and move to next node
            before.next = curr
            before = before.next
        else:
            # Point after's next pointer to curr and move to next node
            after.next = curr
            after = after.next
        # Move pointer to next node
        curr = curr.next

    # Connect the two partitions
    before.next = after_head.next
    after.next = None

    return before_head.next


my_linked_list = LinkedList(1)
my_linked_list.insert_at_end(3)
my_linked_list.insert_at_end(2)
my_linked_list.insert_at_end(23)
my_linked_list.insert_at_end(4)
my_linked_list.insert_at_end(7)
my_linked_list.insert_at_end(12)
my_linked_list.insert_at_end(11)
my_linked_list.insert_at_end(5)
parititoned = partition_list(my_linked_list, 6)
print(parititoned)
