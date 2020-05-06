class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.next = None

# 带空头节点的链表

class LinkList:
    def __init__(self, li):
        self.create_linklist_head(li)

    def create_linklist_head(self, li):
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


if __name__ =="__main__":
    linknote = LinkList([1,2,3,4,5,6])
    linknote.travser_linklist()









#头插法
# for list [1, 2, 3], head ->[1]