'''
Dynamic programming
1)最优子结构， e.g递推表达式， 递归函数问题，函数重复计算，执行效率低

'''
from cal_time import *

def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibnacci(n-1) + fibnacci(n-2)

def fibonacci_non_rec(n):
    f = [0,1,1]
    if n > 2:
        for i in range(n-2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]

# print(fibonacci_non_rec(100))


#钢条切割问题
'''
假设长度尾n的钢条切割后最优收益为Rn， 递推公式为
Rn = max（Pn， R1+Rn-1， R2+Rn-2，... , Rn-1 +R1)
将钢条切割为长度为i和n-i两段
方案i的收益为切割两段的收益之和
'''

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def cut_rod_recursion_1(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_recursion_1(p, i) + cut_rod_recursion_1(p, n-i))
        return res

@cal_time
def cut_rod_recursion(p, n):
    return cut_rod_recursion_1(p, n)

def cut_rod_recursion_2(p, n):
    pass


print(cut_rod_recursion(p, 9))

