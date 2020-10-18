import random

li = list(range(100))

random.shuffle(li)


def quick_sort(li):
    if len(li) < 2:
        return li

    tem = li[0]
    left = [v for v in li[1:] if v < tem]
    right = [v for v in li[1:] if v > tem]
    left = quick_sort(left)
    right = quick_sort(right)

    return left + [tem] + right



def quick_sort2(li):
    if len(li) < 2:
        return li
    tem = li[0]
    left_set = [v for v in li[1:] if v < tem]
    right_set =[v for v in li[1:] if v > tem]
    left_set = quick_sort2(left_set)
    right_set= quick_sort2(right_set)
    return left_set + [tem] + right_set

import sys

def main():
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f)



if __name__ == "__main__":
    main()
