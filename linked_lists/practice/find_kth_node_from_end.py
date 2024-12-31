# Find kth node from end of linked list
# Example:
#   LinkedList: 1 --> 2 --> 3 --> 4 --> 5
#   k = 2
#   kth node = 4 because it is the 2nd node from the end
from linked_lists.implementation import LinkedList


def find_kth_from_end(linked_list, k):
    slow = linked_list.head
    fast = slow
    # Make fast k nodes ahead of slow
    for _ in range(k):
        # Not enough nodes in list
        if fast is None:
            return None
        fast = fast.next
    # Once fast reaches the end, slow will be k nodes distance from the end
    while fast:
        slow = slow.next
        fast = fast.next
    return slow


my_linked_list = LinkedList(1)
my_linked_list.insert_at_end(2)
my_linked_list.insert_at_end(3)
my_linked_list.insert_at_end(4)
my_linked_list.insert_at_end(5)


result = find_kth_from_end(my_linked_list, 2)
print(result.value)
