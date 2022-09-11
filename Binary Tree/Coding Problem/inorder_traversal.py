"""
94. Binary Tree Inorder Traversal:

Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

# iterative 

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    if root is None:
        return []
    values = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        values.append(cur.val)
        cur = cur.right
    return values


a = Node(1)
b = Node(2)
c = Node(5)
d = Node(3)
e = Node(4)

a.left = b
a.right = c
b.left = d
b.right = e

print(inorder(a))
print(inorder(None))



# recursive

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    if root is None:
        return []
    left_side = inorder(root.left)
    right_side = inorder(root.right)
    # return [*left_side, root.val, *right_side]
    return left_side + [root.val] + right_side


a = Node(1)
b = Node(2)
c = Node(5)
d = Node(3)
e = Node(4)

a.left = b
a.right = c
b.left = d
b.right = e

print(inorder(a))
print(inorder(None))



# terative

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    if root is None:
        return []

    values = []
    stack = []
    curr = root

    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            values.append(curr.val)
            curr = curr.right
    return values


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)

a.left = b
a.right = c
b.left = d
c.left = e
c.right = f
e.left = g
e.right = h

print(inorder(a))
