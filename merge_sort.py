'''
归并排序， 分段有序的数列
分解： 将列表越分越小，直到分成一个元素 -》有序
合并：

'''

from cal_time import *
import random
li = list(range(1000))
random.shuffle(li)





def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high: #只要左右都有数字

        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1

    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp




def merge_sort(li, low, high):
    if low < high: #至少两个元素，递归
        mid  = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)


print(li)
merge_sort(li, 0 , len(li)-1)
print(li)