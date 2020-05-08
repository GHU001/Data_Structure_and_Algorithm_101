from _collections import deque

class BiTreeNode(object):

    def __init__(self, data= None):
        self. data = data
        self.lchild = None
        self.rchild = None

A = BiTreeNode('A')
B = BiTreeNode('B')
C = BiTreeNode('C')
D = BiTreeNode('D')
E = BiTreeNode('E')
F = BiTreeNode('F')
G = BiTreeNode('G')



#前序遍历、中序遍历、后序遍历、层次遍历
def pre_order(root):
    if root:
        print(root.data, end='')
        pre_order(root.lchild)
        pre_order(root.rchild)

def in_order(root):
    if root:

        in_order(root.lchild)
        print(root.data, end='')
        in_order(root.rchild)

def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end='')
        in_order(root.rchild)

def level_order(root):
    q = deque()
    q.append(root)
    while(len(q)):
        x = q.popleft()
        print(x.data, end='')
        if x.lchild:
            q.append(x.lchild)
        if x.rchild:
            q.append(x.rchild)
