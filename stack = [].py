# ==========================
# Stack Class Implementation
# ==========================
class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.capacity

    def push(self, item):
        if self.isFull():
            raise Exception("Stack Overflow!")
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack Underflow!")
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty!")
        return self.items[-1]

    def size(self):
        return len(self.items)


# ==========================
# Example 1: Stack Test
# ==========================
print("=== Stack Test ===")
s = Stack(5)
s.push(1)
s.push(2)
s.push(3)
print("Stack:", s.items)
print("Peek:", s.peek())
print("Pop:", s.pop())
print("After pop:", s.items)
print("Size:", s.size())
print()


# ==========================
# Example 2: Reverse String
# ==========================
def reverse_string(text):
    stack = []
    for ch in text:
        stack.append(ch)
    result = ""
    while stack:
        result += stack.pop()
    return result


print("=== Reverse String ===")
print("HELLO ->", reverse_string("HELLO"))
print("PYTHON ->", reverse_string("PYTHON"))
print()


# ==========================
# Example 3: Bracket Checker
# ==========================
def check_brackets(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expression:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack


print("=== Bracket Checker ===")
print("(a+b)        ->", check_brackets("(a+b)"))       # True
print("((a+b]       ->", check_brackets("((a+b]"))      # False
print("{[()]}       ->", check_brackets("{[()]}"))      # True
print("{[(])}       ->", check_brackets("{[(])}"))      # False
