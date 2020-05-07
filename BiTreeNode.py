class BiTreeNode(object):

    def __init__(self, data= None):
        self. data = data
        self.lchild = None
        self.rchild = None

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