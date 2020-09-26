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
    def query(self, node, val):
        if not node:
            return None

        if val > node.data:
            return self.query(node.rchild, val)
        elif val < node.data:
            return self.query(node.left, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    def __remove_node_1(self, node):
        #情况1： node是叶子节点，直接删
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:
            node.parent.lchild = None
            # node.parent = None
        elif node == node.parent.rchild:
            node.parent.rchild = None
            #node.parent = None

    def __remove_node_21(self, node):
        #node只有一个左孩子

        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        elif node == node.parent.rchild:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        #only right child
        if not node.parent:
            self.root = node.rchild
            node.rchild.parent = None

        if node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent









    def delete(self, val):
        if self.root: #not empty tree
            node = self.query_no_rec(val)
            if not node: # not exist
                return False
            if not node.lchild and not node.rchild:#
                self.__remove_node_1(node)
            elif node.lchild and not node.rchild: #2.1
                self.__remove_node_21(node)
            elif not node.lchild and node.rchild: #2.2
                self.__remove_node_22(node)
            else: #两个节点
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data

                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)












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



