"""
Binary Search Tree

"""

class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None

class BST(object):

    def __init__(self, li = None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)


    def insert(self, node, value):
        if not node:
            node = BiTreeNode(value)
        elif value < node.data:
            node.lchild = self.insert(node.lchild, value)
            node.lchild.parent = node
        elif value > node.data:
            node.rchild = self.insert(node.rchild, value)
            node.rchild.parent = node
        return node

    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:

            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return

            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    def pre_order(self, root):
        if root:
            print(root.data, end=' ')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)

            self.post_order(root.rchild)
            print(root.data, end=' ')

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=' ')
            self.in_order(root.rchild)




import random
from collections import deque

li = list(range(100))
random.shuffle(li)

bst = BST(li)
bst.in_order(bst.root)



