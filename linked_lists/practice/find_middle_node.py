# Find middle node of a linked list
# Example: 1 --> 2 --> 3 --> 4 --> 5 ==> middle node is 3
from linked_lists.implementation import LinkedList


def find_middle_node(linked_list):
    slow = linked_list.head
    fast = slow
    # If slow moves 1, fast moves 2
    # So once fast reaches the end, slow should be in the middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


my_linked_list = LinkedList(1)
my_linked_list.insert_at_end(2)
my_linked_list.insert_at_end(3)
my_linked_list.insert_at_end(4)
my_linked_list.insert_at_end(5)

print(find_middle_node(my_linked_list).value)
