# Use a stack to reverse a string

from stacks_and_queues.practice.is_balanced_parentheses import Stack


def reverse_string(my_str):
    stack = Stack()
    for char in my_str:
        stack.push(char)
    new_str = ""
    while not stack.is_empty():
        new_str += stack.pop()
    return new_str


print(reverse_string("hello"))
