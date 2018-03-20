class Stack(object):
    def __init__(self):
        self.items = []
    # isEmpty() tests to see whether the stack is empty.
    # It needs no parameters and returns a boolean value.
    def isEmpty(self):
        return self.items == []
    # push(item) adds a new item to the top of the stack.
    #  It needs the item and returns nothing.
    def push(self, item):
        self.items.append(item)
    # pop() removes the top item from the stack.
    # It needs no parameters and returns the item. The stack is modified.
    def pop(self):
        return self.items.pop()
    # peek() returns the top item from the stack but does not remove it.
    # It needs no parameters. The stack is not modified.
    def peek(self):
        return self.items[len(self.items) -1]
    # size() returns the number of items on the stack.
    # It needs no parameters and returns an integer.
    def size(self):
        return len(self.items)




s = Stack()
print (s.isEmpty())

s.push(1)

print(s.peek())

s.push('two')

print(s.peek())

s.push(True)

print(s.size())

print (s.isEmpty())

print(s.pop())
print(s.pop())
print(s.pop())
print (s.isEmpty())
