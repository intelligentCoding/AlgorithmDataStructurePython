# Write a function that takes a head node and an integer value n and then returns
#  the nth to last node in the linked list. For example, given:
class Node():
    def __init__(self, value):
        self.value = value
        self.nextnode  = None

def nth_to_last_node(n, head):
    left_pointer = head
    right_pointer = head

    for i in range(n-1):
        # Edge case check.

        if not right_pointer.nextnode:
            raise LookupError('N is larger than the linked list')

        right_pointer = right_pointer.nextnode


    while right_pointer.nextnode:

        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer.value

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(4, a)
print(target_node)
