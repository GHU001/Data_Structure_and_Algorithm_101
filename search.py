li = [1,3, 4,5,6,7,10]



def linear_search(data_set, value):
    for index,val in enumerate(data_set):
        if val == value:
            return index
    return

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






#bubble sort
def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(i)- i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            break



#####
#select sort

def min_pos(li):
    min_pos = 0
    for i in range(1, len(li)):
        if li[i] < li[min_pos]:
            min_pos = i

    return min_pos

def select_sort(li):
    for i in range(len(li)):
        min_po = min_pos(li[i:]) + i

        li[i], li[min_po] = li[min_po], li[i]
    return li


#print(select_sort(li))

#insert sort


def insert_sort(li):
    for i in range(1, len(li)):
        tem = li[i]
        j = i -1
        while j >= 0 and li[j] > tem:
            li[j+1] = li[j]
            j -= 1
        li[j + 1] = tem






