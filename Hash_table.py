"""
Hashtable
Hash冲突，链表方法解决

"""

class LinkList(object):

    class Node:
        def __init__(self, item = None):
            self.item = item
            self.next = None

    class LinkListIterator(object):
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                current_node = self.node
                self.node = current_node.next
                return current_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

        
