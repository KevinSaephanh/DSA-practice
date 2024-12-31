# Partition a linked list such that all nodes with values less than x come before
# nodes with values greater than or equal to x
# Example:
#   Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1
#   x: 5
#   3 -> 2 -> 1 -> 8 -> 5 -> 10
from linked_lists.implementation import LinkedList


# Converts a linked list to a list
def to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result


def partition_list(linked_list, x):
    return


my_linked_list = LinkedList(1)
my_linked_list.insert_at_end(3)
my_linked_list.insert_at_end(2)
my_linked_list.insert_at_end(23)
my_linked_list.insert_at_end(4)
my_linked_list.insert_at_end(7)
my_linked_list.insert_at_end(12)
my_linked_list.insert_at_end(11)
my_linked_list.insert_at_end(5)
partition_list(my_linked_list, 6)
