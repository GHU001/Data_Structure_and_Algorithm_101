
def change(t, n):
    m = [0 for _ in range(len(t))]
    for i, num in enumerate(t):
        m[i] = n // num
        n = n % num
    return m, n

t = [100, 50, 10,5,1]

print(change(t, 467))

