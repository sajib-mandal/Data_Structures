class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class Doubly_Link_List:
    def __init__(self):
        self.head = None


    # Insert a "Node" at the head
    def inserAtStart(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
