class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


    # tree insertion
    def insert(self, data):
        if self.data == data:
            return False
        elif data < self.data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True



    # tree Minimum value
    '''''def minValueNode(self, node):
        while node.left != None:
            node = node.left
        return node'''''

    def minValueNode(self, node):
        current = node
        while current.leftChild is not None:
            current = current.leftChild
        return current

    # tree Maximum
    '''''def maxValueNode(self, node):
        while self.right != None:
            node = self.right
        return node'''''

    def maxValueNode(self, node):
        current = node
        while current.rightChild is not None:
            current = current.rightChild
        return current

    # delete a node
    def delete(self, data, root):
        if self is None:
            return None
        if data < self.data:
            self.leftChild = self.leftChild.delete(data, root)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data, root)

        else:
            # deleting node with one child
            if self.leftChild is None:
                if self == root:
                    temp = self.minValueNode(self.rightChild)
                    self.data = temp.data
                    self.rightChild = self.rightChild.delete(temp.data, root)
                temp = self.rightChild
                self = None
                return temp

            elif self.rightChild is None:
                if self == root:
                    temp = self.maxValueNode(self.leftChild)
                    self.data = temp.data
                    self.leftChild = self.leftChild.delete(temp.data, root)
                temp = self.leftChild
                self = None
                return temp
            
            # deleting node with one child
            # first get the inorder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data, root)

        return self



    # tree successor
    def successor(self, x):
        if x.right != None:
            return self.maxValueNode(x.right)
        y = x.parent                               # if confussion https://www.youtube.com/watch?v=YnEF4yfkchs
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y

    # tree predecessor
    def predecessor(self, x):
        if x.left != None:
            return self.minValueNode(x.left)
        y = x.parent
        while y != None and x == y.left:
            x = y
            y = y.parent
        return y


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

    '''''def inorder(root):
        if root:
            inorder(root.left)
            print(root.val)
            inorder(root.right)'''''

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(self.data)
            if self.rightChild:
                self.rightChild.inorder()

    def preorder(self):
        if self:
            print(self.data)
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(self.data)


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data,self.root)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()

if __name__ == '__main__':
    tree = Tree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(4)
    tree.insert(20)
    tree.insert(8)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    print(tree.find(1))
    print(tree.find(12))
    ''''' Following tree is getting created:
                    10
                 /      \
               5         12
              / \           \
            4     8          20
                 /          /
                7         15
                         /
                       13
    '''''

    tree.preorder()
    tree.inorder()
    tree.postorder()
    print('\n\nAfter deleting 20')
    tree.delete(20)
    tree.inorder()
    tree.preorder()
    print('\n\nAfter deleting 10')
    tree.delete(10)
    tree.inorder()
    tree.preorder()
