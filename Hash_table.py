"""
Hashtable
Hash冲突，链表方法解决

"""

class LinkList(object):

    class Node:
        def __init__(self, item = None):
            self.item = item
            self.next = None

    class LinkListIterator:

        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                curNode = self.node
                self.node = curNode.next
                return curNode.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self,iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s


    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
            else:
                return False


    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "<<" + ", ".join(map(str, self)) + ">>"

li = [1,2,3,4]
listnode = LinkList(li)
print(listnode)





        
