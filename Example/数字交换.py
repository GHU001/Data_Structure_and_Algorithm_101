'''

拼接最大整数

'''
from functools import cmp_to_key
li = [32, 94, 87, 128, 1286, 728, 7286, 9]
def xy_cmp(x, y):
    if x+y > y+x:
        return -1
    elif x+y < y+x:
        return 1
    else:
        return 0

def largest_cont_number(li):
    li = list(map(str, li))
    li.sort(key=cmp_to_key(xy_cmp))
    return "".join(li)

print(largest_cont_number(li))


'''
活动选择问题
每个活动都有一个开始时间Si和结束时间fi，安排那些活动能使场地举办的活动最多
'''

