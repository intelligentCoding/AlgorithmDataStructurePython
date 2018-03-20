# Implement a Deque
# Implement a Deque class! It should be able to do the following:
#
# Check if its empty
# Add to both front and rear
# Remove from Front and Rear
# Check the Size

class Deque(object):
    # Default constructor declares a list "items"
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.append(0, item)

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)
