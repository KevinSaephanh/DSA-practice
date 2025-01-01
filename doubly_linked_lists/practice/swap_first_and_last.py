# Swap the values of the first and last nodes of a doubly linked list
# Example: 1 <--> 2 <--> 3 <--> 4 ==> 4 <--> 2 <--> 3 <--> 1


from doubly_linked_lists.implementation import DoublyLinkedList


def swap_first_last(dll):
    if dll.head is None or dll.head.next is None:
        return None
    dll.head.value, dll.tail.value = dll.tail.value, dll.head.value


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
my_doubly_linked_list.append(6)
swap_first_last(my_doubly_linked_list)
my_doubly_linked_list.print_list()
