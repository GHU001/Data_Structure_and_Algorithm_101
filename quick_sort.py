li = [1,3,2,4,1,5,5,4,3]

a = 0
for i in li:
    a = a ^ i
print(a)


######
#quick sort

def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid -1)
        quick_sort(li, mid + 1, right)


def partition(li, left, right):

    tem = li[left]

    while left < right:
        while li[right] > tem:
            right -= 1
        li[left] = li[right]

        while li[left] < tem:
            left += 1
        li[right] = li[left]
    return left


