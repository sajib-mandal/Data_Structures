class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d


# A -> B -> C -> D -> None

# iterative solution on linked list
def iterative_print_list(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next

iterative_print_list(a)

print("new list")


# recursive solution on linked list

def recursive_print_list(head):
    if head is None:
        return
    print(head.val)
    recursive_print_list(head.next)

recursive_print_list(a)
