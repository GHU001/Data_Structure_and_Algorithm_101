'''
Dynamic programming
1)最优子结构， e.g递推表达式， 递归函数问题，函数重复计算，执行效率低

'''
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