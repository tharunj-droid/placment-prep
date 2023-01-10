"""Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"""

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)
        return Stack

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isEmpty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


s=Stack()
s.push(20)
print(s.peek())
s.push(290)
print(s.peek())
s.pop()
print(s.peek())
# excersice problem of reversing a stack

def reverse_string(s):
    stack=Stack()
    for ch in s:
            stack.push(ch)
    rev_string=''
    while stack.size()!=0:
        rev_string+=stack.pop()

    return rev_string


if __name__ == '__main__':
    print("hello")
    print(reverse_string("this is tharun"))

# problem to check if no of paranthesis is equal


def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def check_paranthesis(string):
    stack = Stack()
    for ch in string:
        if (ch == '(' or ch == '{' or ch == '['):
            stack.push(ch)
        elif (ch == '}' or ch == ']' or ch == ')'):

            if stack.size() == 0:
                return False
            if not is_match(ch, stack.pop()):
                return False
            else:
                return True

    return stack.size == 0


if __name__ == '__main__':
    print(check_paranthesis("({a+b})"))
    print(check_paranthesis("))((a+b}{"))
    print(check_paranthesis("((a+b))"))
    print(check_paranthesis("((a+g))"))
    print(check_paranthesis("))"))
    print(check_paranthesis("[a+b]*(x+2y)*{gg+kk}"))
