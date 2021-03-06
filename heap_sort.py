def sift(li, low, high):
    """


    :param li: 列表
    :param low: 堆根结点的位置
    :param high: 堆最后一个元素的位置
    :return:
    """

    i = low   #i是最开始节点位置
    j = 2 * i + 1 #左节点
    tmp = li[low] #把堆顶存起来

    while j <= high: #只要j位置有数
        if j + 1 <= high and li[j+1] > li[j]:  #有右节点，并且右节点位置大于左节点
            j = j + 1 #j指向右节点
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else: #tmp更大
            li[i] = tmp
            break
    else:
        li[i] = tmp





def sift(li, low, high):
    """


    :param li: 列表
    :param low: 堆根结点的位置
    :param high: 堆最后一个元素的位置
    :return:
    """

    i = low   #i是最开始节点位置
    j = 2 * i + 1 #左节点
    tmp = li[low] #把堆顶存起来

    while j <= high: #只要j位置有数
        if j + 1 <= high and li[j+1] > li[j]:  #有右节点，并且右节点位置大于左节点
            j = j + 1 #j指向右节点
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else: #tmp更大
            break
    li[i] = tmp

def heap_sort(li):
    n = len(li)
    #建堆
    for i in range((n - 2)//2, -1, -1):
        sift(li, i, n - 1)

    for i in range(n, -1, -1):
        #i 指向当前堆的最大位置
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1) #i-1 是新的high

'''
heapq
heapq.heapify(li)
heapq.heappop(li)
'''


'''
top k
现有n个数，算法得到前最k大的问题
1)思路 排序 + 切片 O（nlogn）
2）冒泡 k趟 O（kn）

3）堆排序 O（nlogk）
'''




def sift_small_heap(li, low, high):
    """

     小根堆
    :param li: 列表
    :param low: 堆根结点的位置
    :param high: 堆最后一个元素的位置
    :return:
    """

    i = low   #i是最开始节点位置
    j = 2 * i + 1 #左节点
    tmp = li[low] #把堆顶存起来

    while j <= high: #只要j位置有数
        if j + 1 <= high and li[j+1] < li[j]:  #有右节点，并且右节点位置大于左节点
            j = j + 1 #j指向右节点
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else: #tmp更大
            break
    li[i] = tmp


def topk(li):
    heap = li[0:k]
    for i in range((k - 2)//2, -1, -1):
        sift_small_heap(heap, i, k-1)
        #1. 建堆
    
