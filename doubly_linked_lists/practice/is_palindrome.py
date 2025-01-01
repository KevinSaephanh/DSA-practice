# Check if a doubly linked list is a palindrome (same spelling forwards and backwards)
# Example:
#   Palindrome: 1 <--> 2 <--> 3 <--> 2 <--> 1
#   NOT Palindrome: 1 <--> 2 <--> 3 <--> 4 <--> 3


from doubly_linked_lists.implementation import DoublyLinkedList


def is_palindrome(dll):
    my_str = ""
    curr = dll.head
    while curr:
        # Append value to string
        my_str += str(curr.value)
        curr = curr.next
    # Check if string is equal to its reversed string
    return my_str == my_str[::-1]


my_doubly_linked_list1 = DoublyLinkedList(1)
my_doubly_linked_list1.append(2)
my_doubly_linked_list1.append(3)
my_doubly_linked_list1.append(4)
my_doubly_linked_list1.append(5)
my_doubly_linked_list1.append(4)
my_doubly_linked_list1.append(3)
print(is_palindrome(my_doubly_linked_list1))


my_doubly_linked_list2 = DoublyLinkedList(1)
my_doubly_linked_list2.append(2)
my_doubly_linked_list2.append(3)
my_doubly_linked_list2.append(2)
my_doubly_linked_list2.append(1)
print(is_palindrome(my_doubly_linked_list2))
