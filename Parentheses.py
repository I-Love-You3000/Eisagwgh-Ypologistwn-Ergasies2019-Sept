class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


s = Stack()
code = input('Please enter code: ')

for c in code:
    if c == '(':
        s.push(1)
    elif c == ')':
        if s.is_empty():
            correct = False
            break
        s.pop()
else:
    if s.is_empty():
        correct = True
    else:
        correct = False

if correct:
    print('Code is correctly parenthesized.')
else:
    print('Code is not correctly parenthesized.')