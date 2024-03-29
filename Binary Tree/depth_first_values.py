"""
Depth First Search:
Write a function, depth_first_values, that takes in the root of a binary tree.
The function should return a list containing all values of the tree in depth-first
order.

Hey. This is our first binary tree problem, so you should be liberal with watching
the Approach and Walk-through. Be productive, not stubborn. -AZ
"""

# iterative version

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def depth_first_values(root):
    if root is None:
        return []

    values = []
    stack = [root]

    while stack:
        current = stack.pop()
        values.append(current.val)

        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return values
  

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
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

print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'c', 'f']


# recursive version

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def depth_first_values(root):
    if root is None:
        return []
    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)
    # return [root.val, *left_values, *right_values]
    return [root.val] + left_values + right_values      # both return value is work correctly


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
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

print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'c', 'f']

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']

a = Node('a')
#     a
print(depth_first_values(a))
#   -> ['a']

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.right = b
b.left = c
c.right = d
d.right = e

#      a
#       \
#        b
#       /
#      c
#       \
#        d
#         \
#          e

print(depth_first_values(a))
#   -> ['a', 'b', 'c', 'd', 'e']

print(depth_first_values(None))
#   -> []
