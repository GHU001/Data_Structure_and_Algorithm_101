'''

欧几里得算法

'''

def gcd(a,b):
    if b == 0:
        return a
    while b:
        return gcd(b, a%b)


def gcd2(a,b):
    while b:
        r = a%b
        a = b
        b = r
    return a


print(gcd2(64,16))
