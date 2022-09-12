class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_identical(x, y):
    if x is None and y is None:
        return True

    if x is None or y is None:      # if x is None or y is None or x.val != y.val:
        return False                           # return False

    if x.val != y.val:
        return False

    return is_identical(x.left, y.left) and is_identical(x.right, y.right)

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

a1 = Node(1)
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



# iterative

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_identical(x, y):
    if x is None and y is None:
        return True

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        if x.val != y.val:
            return False

        if x.left and y.left:
            queue.append((x.left, y.left))

        elif x.left or y.left:
            return False

        if x.right and y.right:
            queue.append((x.right, y.right))
        elif x.right or y.right:
            return False
    return True


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

a1 = Node(1)
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
