class Queue (object):
    def __init__(self):
        self.items = []


# Queue() creates a new queue that is empty.
# It needs no parameters and returns an empty queue.
# enqueue(item) adds a new item to the rear of the queue.
# It needs the item and returns nothing.
    def enqueue(self, item):
        self.items.insert(0, item)
# dequeue() removes the front item from the queue.
# It needs no parameters and returns the item. The queue is modified.
    def dequeue (self):
        return self.items.pop()
# isEmpty() tests to see whether the queue is empty.
#  It needs no parameters and returns a boolean value.
    def isEmpty(self):
        return self.items == []

# size() returns the number of items in the queue.
# It needs no parameters and returns an integer.
    def size(self):
        return len(self.items)


q = Queue()

q.size()

q.isEmpty()

q.enqueue(1)

q.enqueue(2)

# what item will come out...
print(q.dequeue())
# it will be one.