class Stack:

    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if len(self.values) > 0:
            return self.values.pop()
        else:
            print('Empty Stack')

    def peek(self):
        if len(self.values) > 0:
            return self.values[-1]
        else:
            print('Empty Stack')
            return None

    def is_empty(self):
        if len(self.values) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.values)


s = Stack()
s.peek()
print(s.is_empty())
s.push('cat')
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(777)
print(s.pop())
print(s.pop())
print(s.size())

