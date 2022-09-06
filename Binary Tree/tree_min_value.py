"""
Tree Min Value:
Write a function, tree_min_value, that takes in the root of a binary
tree that contains number values. The function should return the minimum
value within the tree.

You may assume that the input tree is non-empty.
"""

# iterative depth_first_traversal

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_min_value(root):
    smallest = float("inf")
    stack = [root]

    while stack:
        current = stack.pop()
        if current.val < smallest:
            smallest = current.val

        if current.left is not None:
            stack.append(current.left)

        if current.right is not None:
            stack.append(current.right)

    return smallest


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
print(tree_min_value(a))  # -> -2



# iterative breadth_first_traversal
