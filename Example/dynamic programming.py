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

最优子结构： 问题的最优解由相关子问题的最优解组合而成，这些子问题可以独立求解
'''

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 38, 39, 40, 45,47]

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
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n+1):
            res = max(res, p[i] + cut_rod_recursion_2(p, n-i))
    return res


@cal_time
def cut_rod_recursion2(p, n):
    return cut_rod_recursion_2(p, n)


# print(cut_rod_recursion(p, 13))
# print(cut_rod_recursion2(p, 13))
#自底向上的实现,先算1，2，3，。。。

@cal_time
def cut_rod_dp(p, n):
    r = [0]
    if n == 0:
        return 0

    for i in range(1, n + 1):
        res = 0
        for j in range(1, i + 1):
            res = max(res, p[j] + r[i - j])
        r.append(res)
    return r[n]


def cut_rod_extend(p,n):
    r = [0]
    s = [0]


    for i in range(1, n + 1):
        res_r = 0
        res_s = 0

        for j in range(1, i + 1):
            if p[j] + r[i - j]:
                res_r = p[j] + r[i - j]
                res_j = j

        r.append(res_r)
        s.append(res_j)
    return r[n], s

def cut_dor_solution(p,n):
    r,s = cut_rod_extend(p,n)

    ans = []
    while n>0:
        ans.append(r[n])
        n -= r[n]
    return ans

# print(cut_rod_dp(p,10))

#longest common string
def lcs_length(x, y):
    m = len(x)
    n = len(y)
    c =[[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c[m][n]


