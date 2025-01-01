# Reverse a doubly linked list
# Example: 1 <--> 2 <--> 3 <--> 4 ==> 4 <--> 3 <--> 2 <--> 1

from doubly_linked_lists.implementation import DoublyLinkedList


def reverse(dll):
    if dll.length <= 1:
        return None
    curr = dll.head
    while curr:
        # Swap pointers of prev and next for curr's next and prev
        curr.next, curr.prev = curr.prev, curr.next
        curr = curr.prev
    # Swap head and tail
    dll.head, dll.tail = dll.tail, dll.head


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
my_doubly_linked_list.append(6)
reverse(my_doubly_linked_list)
my_doubly_linked_list.print_list()
