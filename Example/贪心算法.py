
def change(t, n):
    m = [0 for _ in range(len(t))]
    for i, num in enumerate(t):
        m[i] = n // num
        n = n % num
    return m, n

# t = [100, 50, 10,5,1]

# print(change(t, 467))


'''
背包问题

0-1 背包

分数背包

'''
goods = [(60,10), (100,20), (120,30)]

def fractional_bagpack(goods, w):
    goods.sort(key=lambda x:x[0]/x[1], reverse=True)
    m = [0 for _ in range(len(goods))]
    for i, (price, weight) in enumerate(goods):
        if w > weight:
            m[i] = 1
            w -= weight
        else:
            m[i] = w / weight
            w = 0
    return m
print(fractional_bagpack(goods, 45))



