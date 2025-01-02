# Check to see if a string of parentheses is balanced or not.
# By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order.
# Examples:
#   Balanced: ((()))
#   NOT Balanced: ((()


class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        return None if self.is_empty() else self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        return None if self.is_empty() else self.stack_list.pop()


def is_balanced_parentheses(parentheses):
    left = Stack()
    right = Stack()
    for char in parentheses:
        if char == "(":
            left.push(char)
        else:
            right.push(char)
    return left.size() == right.size()


print(is_balanced_parentheses("((()))"))
print(is_balanced_parentheses("((()"))
