'''
Stack last in first out,
栈顶， 栈底

进站 push
出战 pop
取站顶 gettop

top




bottom

进站  li.append()
出战   li.pop
取站顶  li[-1]

'''

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

def brackets_match(s):
    match = {')':'(', ']':'[', '}':'{'}
    stack = Stack()

    for ch in s:
        if ch in['[','{','(']:
            stack.push(ch)
        else: # ch in [0, ],}]
            if stack.is_empty():
                return False
            elif match[ch] == stack.get_top():
                stack.pop()
            else:
                return False







#Queue
'''

rear = (rear +1)%length
front = (front +1)%length

empty  rear == front
full   (rear +1) % length == front


两个队列，
进队 -》 一号栈进栈
出对      二号站出栈，如果二号栈空，把一号栈一次出栈，并进二号栈

'''

from collections import deque
import numpy as np


#solve maze

dirs =[

    lambda x, y: (x-1, y), # up
    lambda x, y: (x, y+1),# right
    lambda x, y: (x+1, y), # down
    lambda x, y: (x, y-1) # left


]

maze = np.random.randint(2, size=64).reshape(8,8)
print(maze)


def solve_maze(x1, y1, x2, y2):

    stack = []

    stack.append((x1,y1))

    while len(stack) > 0:
        curr_node = stack[-1]
        if curr_node == (x2, y2):
            print(stack)
            return True

        for d in dirs:
            next_node = d(*curr_node)
            if maze[next_node[0]][next_node[1]] == 0:
                stack.append(next_node)
                maze[next_node[0]][next_node[1]] = 2
                break
        else:
            stack.pop()
    print("No route out")
    return False


solve_maze(1,1,4,4)

