import sys

class Node():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1       # 1==> red and 0==> black


class RedBlackTree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL


    def pre_order_helper(self, node):
        if node != self.TNULL:
            sys.stdout.write(node.data + " ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)


    def in_order_helper(self, node):
        if node != self.TNULL:
            self.in_order_helper(node.left)
            sys.stdout.write(node.data + " ")
            self.in_order_helper(node.right)


    def post_order_helper(self, node):
        if node != self.TNULL:
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)
            sys.stdout.write(node.data + " ")


    def search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.data:
            return node
        if key < node.data:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)


    def fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

            # case 3.2
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent

            # case 3.3
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.right

                # case 3.4
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root

            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent

                else:
                    if self.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = s.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0





    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotaate(k)
                        k.parent.color = 0
                        k.parent.parent.color = 1
                        self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)

            if k == self.root:
                break
        self.root.color = 0



    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y



    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y


    # Insertion key on red-black Tree

    def insert(self, key):
       node = Node(key)
       node.parent = None
       node.data = key
       node.left = self.TNULL
       node.right = self.TNULL
       node.color = 1


       y = None
       x = self.root

       while x !=self.TNULL:
           y = x
           if node.data < x.data:
               x = x.left
           else:
               x = x.right


       node.parent = y
       if y == None:
           self.root = node
       elif node.data < y.data:
           y.left = node
       else:
           y.right = node


       if node.parent == None:
           node.color = 0
           return

       if node.parent.parent == None:
           return
