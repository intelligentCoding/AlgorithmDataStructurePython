class DoublyLinkedListNode(object):

    def __init__(self,value):

        self.value = value
        self.next_node = None
        self.prev_node = None


a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)
# Setting b after a
b.prev_node = a
a.next_node = b
# Setting c after a
b.next_node = c
c.prev_node = b