# li = [1,3,2,4,1,5,5,4,3]
#
# a = 0
# for i in li:
#     a = a ^ i
# print(a)


######
#quick sort
import random

li = list(range(1000))
random.shuffle(li)
# li.append(1)

def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid -1)
        quick_sort(li, mid + 1, right)


def partition(li, left, right):

    tem = li[left]

    while left < right:
        while li[right] > tem and left < right:
            right -= 1
        li[left] = li[right]

        while li[left] < tem and left < right:
            left += 1
        li[right] = li[left]
    li[left] = tem
    return left


#


quick_sort(li,0,len(li) - 1)

print(li)

def quick_sort2(li):
    if len(li) < 2:
        return li
    tem = li[0]
    left_set = [v for v in li[1:] if v < tem]
    right_set =[v for v in li[1:] if v > tem]
    left_set = quick_sort2(left_set)
    right_set= quick_sort2(right_set)
    return left_set + [tem] + right_set

