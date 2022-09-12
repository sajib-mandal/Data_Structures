# iterative

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_bottom_left_value(root):

    queue = deque([root])

    while queue:
        current = queue.popleft()

        if current.right:
            queue.append(current.right)

        if current.left:
            queue.append(current.left)

    return current.val


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
c.left = e
c.right = f
e.left = g

print(find_bottom_left_value(a))
