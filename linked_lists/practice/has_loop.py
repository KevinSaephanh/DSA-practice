# Determine if a linked list has a loop:
# Loop Example: 1 --> 2 --> 3 --> 4 --> 1 --> 2...
# Non Loop Example: 1 --> 2 --> 3 --> 4
from linked_lists.implementation import LinkedList


def has_loop(linked_list):
    slow = linked_list.head
    fast = slow
    # If slow moves 1, fast moves 2
    # If there is a loop, fast will eventually equal slow as it moves at double the pace
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # Loop detected
        if slow == fast:
            return True
    # If fast reaches the end, that means the list does not loop on itself
    return False


my_linked_list_1 = LinkedList(1)
my_linked_list_1.insert_at_end(2)
my_linked_list_1.insert_at_end(3)
my_linked_list_1.insert_at_end(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(has_loop(my_linked_list_1))  # Returns True


my_linked_list_2 = LinkedList(1)
my_linked_list_2.insert_at_end(2)
my_linked_list_2.insert_at_end(3)
my_linked_list_2.insert_at_end(4)
print(has_loop(my_linked_list_2))  # Returns False
