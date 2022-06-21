class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # inserting the "Node" at the first

    def insertAtStart(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    # inserting the "Node" at the end

    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newNode

    # inserting the "Node" in between the linked list

    def insertBetween(self, previousNode, data):
        if previousNode.next is None:
            print("Previous node should have next node!")
        else:
            newNode = Node(data)
            newNode.next = previousNode.next
            previousNode.next = newNode

    # searching an item in the list

    def search(self, node, data):
        if node == None:
            return False
        if node.data == data:
            return True
        return self.serach(node.getNext(), data)


    # delete an item in the list

    def delete(self, data):
        temp = self.head

        # if data/key is found in head node itself
        if temp.next is not None:
            if temp.data == data:
             self.head = temp.next
             temp = None
             return
        else:
            # search all the node
            while temp.next != None:
                if temp.data == data:
                    break
                prev = temp
                temp = temp.next

            # "Node" not found
            if temp == None:
                return
            prev.next = temp.next
            return
