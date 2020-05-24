import random

li = list(range(100))

random.shuffle(li)
print(li)

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


li = quick_sort(li)

print(li)



