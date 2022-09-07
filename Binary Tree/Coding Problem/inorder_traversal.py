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
