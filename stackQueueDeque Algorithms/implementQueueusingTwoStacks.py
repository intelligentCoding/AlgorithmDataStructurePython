# Implement a Queue - Using Two Stacks - SOLUTION
# Given the Stack class below, implement a Queue class using two stacks!
# Note, this is a "classic" interview problem. Use a Python list data structure as
# your Stack.

class Queue2Stacks(object):
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    # Because for queue we have FIFO, first-in-first-out we need to reverse
    # the instack for pop() function.

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()


q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())