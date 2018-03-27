def BinaryTree(r):

    return [r,[],[]]

def inserLeft(root, newBranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])

    return root

def inserRight(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])

    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]




r = BinaryTree(3)

print(inserLeft(r,4))
print(inserLeft(r,6))
print(inserRight(r,7))
print(inserRight(r,8))

l = getLeftChild(r)
print(l)
setRootVal(r,9)
print(r)