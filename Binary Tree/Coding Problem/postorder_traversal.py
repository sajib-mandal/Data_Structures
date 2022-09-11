# recursive

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def postorder(root):
    if root is None:
        return []

    left_side = postorder(root.left)
    right_side = postorder(root.right)

    return left_side + right_side + [root.val]


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

print(postorder(a))
