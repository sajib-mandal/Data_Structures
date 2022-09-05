"""
Reverse List:
Write a function, reverse_list, that takes in the head of a linked
list as an argument. The function should reverse the order of the
nodes in the linked list in-place and return the new head of the
reversed linked list.
"""

# iterative reverse list with return new head value

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev.val


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

print(reverse_list(a))  # f -> e -> d -> c -> b -> a

x = Node("x")
y = Node("y")

x.next = y

# x -> y

print(reverse_list(x))  # y -> x

p = Node("p")

# p

print(reverse_list(p))  # p



# recursive reverse list with return new head value

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head, prev = None):
    if head is None:
        return prev.val
    next = head.next
    head.next = prev
    return reverse_list(next, head)



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

print(reverse_list(a))  # f -> e -> d -> c -> b -> a

x = Node("x")
y = Node("y")

x.next = y

# x -> y

print(reverse_list(x))  # y -> x

p = Node("p")

# p

print(reverse_list(p))  # p
