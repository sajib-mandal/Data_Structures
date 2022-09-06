"""
Tree Sum:
Write a function, tree_sum, that takes in the root of a binary tree that
contains number values. The function should return the total sum of all
values in the tree.
"""
# iterative version breadth_first_search

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_sum(root):
    if root is None:
        return 0
    total_sum = 0
    queue = deque([root])

    while queue:
        current = queue.popleft()
        total_sum += current.val

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)
    return total_sum


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(tree_sum(a))  # -> 21




# depth_first_search recursive tree sum

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_sum(root):
    if root is None:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(tree_sum(a))  # -> 21

a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2

print(tree_sum(a))  # -> 10

print(tree_sum(None))  # -> 0
