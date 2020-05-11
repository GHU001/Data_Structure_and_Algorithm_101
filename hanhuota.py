
def hanoi(n, A, B, C):
    if n>0:
        hanoi(n-1, A, C, B)
        print(' from {} to {}'.format(A, C))
        hanoi(n-1, B, A, C)

hanoi(3, 'A', 'B', 'C')
