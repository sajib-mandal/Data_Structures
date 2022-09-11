# recursive


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(root):
    if root is None:
        return []

    left_side = preorder(root.left)
    right_side = preorder(root.right)

    return [root.val] + left_side + right_side


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

print(preorder(a))
