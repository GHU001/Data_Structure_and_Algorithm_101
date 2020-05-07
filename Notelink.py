class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.next = None

# 带空头节点的链表

class LinkList:
    def __init__(self, li, method='tail'):
        self.head = None
        self. tail = None
        if method == 'tail':
            self.create_linklist_tail(li)
        elif method =='head':
            self.create_linklist_head(li)
        else:
            raise TypeError('Unsupported method')
    def create_linklist_head(self, li):#头插法，倒叙
        self.head = Node(0)
        for v in li:
            n = Node(v)
            n.next = self.head.next
            self.head.next = n        #
            self.head.data += 1

    def travser_linklist(self):
        p = self.head.next
        while p:
            print(p.data)
            p = p.next

    def create_linklist_tail(self, li):
        self.head = Node(0)
        self.tail = self.head
        for v in li:
            p = Node(v)
            self.tail.next = p
            self.tail = p
            self.head.data += 1

    def __len__(self):
        return self.head.data







if __name__ =="__main__":
    linknote = LinkList([1,2,3,4,5,6],'tail')
    linknote.travser_linklist()
    print(len(linknote))









#头插法
# for list [1, 2, 3], head ->[1]