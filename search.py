li = [1,3, 4,5,6,7,10]

def bin_search(li, val):
    low = 0
    high = len(li) -1
    while low <= high:
        mid = (low + high)//2
        if li[mid] == val:
            return mid
        elif li[mid] < val:
            low = mid + 1
        else:
            high = mid -1
    return -1

print(bin_search(li, 7))





def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(i)- i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


