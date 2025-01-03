# Sort a stack in ascending order
from stacks_and_queues.practice.is_balanced_parentheses import Stack


def sort_stack(stack):
    my_list = []
    while not stack.is_empty():
        my_list.append(stack.pop())
    my_list.sort()
    for i in range(len(my_list) - 1, -1, -1):
        stack.push(my_list[i])


my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()
