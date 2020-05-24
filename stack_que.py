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

