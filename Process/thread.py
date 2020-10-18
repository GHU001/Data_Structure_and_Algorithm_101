import threading

#multiple thread to change variable
num = 0

def run(n):
    #define global num
    global num
    for i in range(1000000):
        num = num + n
        num = num - n

"""
一个线程操作数据的时候，其他线程不允许操作数据
"""
lock = threading.Lock()

def run2(n):
    global num
    for i in range(1000000):
        with lock:
            num = num + n
            num = num - n


if __name__ == "__main__":

    t1 = threading.Thread(target=run2, args=(6,))
    t2 = threading.Thread(target=run2, args=(10,))

    #start thread
    t1.start()
    t2.start()

    #wait for thread to finish
    t1.join()
    t2.join()

    print('num =', num)

