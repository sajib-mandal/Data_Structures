"""
Tree Includes:
Write a function, tree_includes, that takes in the root of a binary
tree and a target value. The function should return a boolean indicating
whether or not the value is contained in the tree.
"""
# iterative breadth_first_search

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_includes(root, target):
    if root is None:
        return False

    queue = deque([root])
    while queue:
        current = queue.popleft()

        if current.val == target:
            return True

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return False


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(tree_includes(a, "e"))  # -> True
print(tree_includes(a, "a"))  # -> True
print(tree_includes(a, "n"))  # -> False


# iterative depth_first_search

