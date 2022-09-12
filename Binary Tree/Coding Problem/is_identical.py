class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_identical(x, y):
    if x is None and y is None:
        return True

    return (x is not None and y is not None) and (x.val == y.val) and is_identical(x.left, y.left) and is_identical(
        x.right, y.right)


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

a1 = Node(10)
b1 = Node(2)
c1 = Node(3)
d1 = Node(4)
e1 = Node(5)
f1 = Node(6)
g1 = Node(7)

a1.left = b1
a1.right = c1
b1.left = d1
b1.right = e1
c1.left = f1
c1.right = g1

print(is_identical(a, a1))
