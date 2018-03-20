# Singly Linked List Cycle Check
# Problem
# Given a singly linked list, write a function which takes in the
# first node in a singly linked list and returns a boolean indicating
# if the linked list contains a "cycle".
#
# A cycle is when a node's next point actually points back to a
# previous node in the list. This is also sometimes known as a
# circularly linked list.
#
# You've been given the Linked List Node class code:

class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None


def cycle_check(node):
    marker1 = node
    marker2 = node
    counter = 0
    while marker2 != None and marker2.nextnode != None:


        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode
        # print("Marker1 Value =  " + str(marker1.value))
        # print("-"*40)
        # print("Marker2 Value =  " + str(marker2.value))
        # print("-"*40)
        if marker2 == marker1:
            return True
    return False







# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = a # Cycle Here!

print(cycle_check(a))

# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)
print(cycle_check(x))

x.nextnode = y
y.nextnode = z



