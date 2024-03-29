"""
Linked List Values:
Write a function, linked_list_values, that takes in the head of a linked list as an argument.
The function should return a list containing all values of the nodes in the linked list.

Hey. This is our first linked list problem, so you should be liberal with watching the
Approach and Walk-through. Be productive, not stubborn. -AZ
"""

# iterative linked list values

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_values(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_values(a))  # -> [ 'a', 'b', 'c', 'd' ]

x = Node("x")
y = Node("y")

x.next = y

# x -> y

print(linked_list_values(x))  # -> [ 'x', 'y' ]

q = Node("q")

# q

print(linked_list_values(q))  # -> [ 'q' ]

print(linked_list_values(None))  # -> [ ]


# recursive linked list values

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_values(head):
    values = []
    fill_values(head, values)

    return values


def fill_values(head, values):
    if head is None:
        return
    values.append(head.val)
    fill_values(head.next, values)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_values(a))  # -> [ 'a', 'b', 'c', 'd' ]

x = Node("x")
y = Node("y")

x.next = y

# x -> y

print(linked_list_values(x))  # -> [ 'x', 'y' ]

q = Node("q")

# q

print(linked_list_values(q))  # -> [ 'q' ]

print(linked_list_values(None))  # -> [ ]
