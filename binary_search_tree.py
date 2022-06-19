class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


    # tree Minimum value
    def minValueNode(self, node):
        while node.left != None:
            node = node.left
        return node

    # tree Maximum
    def maxValueNode(self, node):
        while node.right != None:
            node = node.right
        return node



    # tree search
    def find(self, data):
        if data == self.data:
            return True

        elif data < self.data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False

        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
