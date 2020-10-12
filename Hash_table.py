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






        
