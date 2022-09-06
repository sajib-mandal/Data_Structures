"""
199. Binary Tree Right Side View:
Given the root of a binary tree, imagine yourself standing on the right
side of it, return the values of the nodes you can see ordered from top
to bottom.
"""

# iterative depth first

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def right_side_view(root):
    if root is None:
        return []
    values = []
    stack = [root]

    while stack:
        current = stack.pop()
        values.append(current.val)
        if current.right is not None:
            stack.append(current.right)

    return values


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.left = b
a.right = c
b.right = e
c.right = d

#       1
#      /  \
#     2    3
#      \    \
#       5    4

print(right_side_view(a))    # [1, 3, 4]


a = Node(1)
b = Node(3)
a.right = b

#      1
#       \
#        3
print(right_side_view(a))  # [1, 3]

print(right_side_view(None))  # []


# iterative breadth first

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def right_side_view(root):
    if root is None:
        return []
    values = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        values.append(current.val)
        if current.right is not None:
            queue.append(current.right)

    return values


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(5)
e = Node(10)
f = Node(4)

a.left = b
a.right = c
b.right = d
c.left = e
c.right = f

#       1
#      /  \
#     2    3
#      \    \
#       5    4

print(right_side_view(a))  # [1, 3, 4]

a = Node(1)
b = Node(3)
a.right = b

#      1
#       \
#        3
print(right_side_view(a))  # [1, 3]

print(right_side_view(None))  # []
