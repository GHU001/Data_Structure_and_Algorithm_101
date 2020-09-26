"""
decorator for cal_time
"""
import time

def cal_time(func):
    def wrapper(*args, **kwargs):
        time1 = time.time()
        result = func(*args, **kwargs)
        time2 = time.time()
        print("%s running time: %s  secs. " % (func.__name__, time2 - time1))
        return result
    return wrapper


