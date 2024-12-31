# Remove all duplicates from the linked list
# Example: 1 --> 2 --> 3 --> 3 --> 2 --> 4 ==> 1 --> 2 --> 3 --> 4
from linked_lists.implementation import LinkedList


def remove_duplicates(linked_list):
    if not linked_list.head or linked_list.head.next:
        return linked_list.head

    seen = set()
    curr = linked_list.head
    prev = None
    while curr:
        if curr.value in seen:
            # Ex: 1 --> 2 --> prev --> curr --> curr.next ==> 1 --> 2 --> prev --> curr.next
            prev.next = curr.next
        else:
            seen.add(curr.value)
            prev = curr
        curr = curr.next


my_linked_list = LinkedList(1)
my_linked_list.insert_at_tail(2)
my_linked_list.insert_at_tail(3)
my_linked_list.insert_at_tail(3)
my_linked_list.insert_at_tail(4)
my_linked_list.insert_at_tail(2)
my_linked_list.insert_at_tail(5)
my_linked_list.insert_at_tail(6)
remove_duplicates(my_linked_list)
print(my_linked_list)
