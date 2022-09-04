# -*- coding: utf-8 -*-
"""
@ Author: Brynhildr Wu
@ Email: brynhildrwu@gmail.com

Multi-threading test.
There is no sequence in the execution of multiple threads.

update: 2022/7/9

"""

# %%
import socket
import threading
import time

# %%
# global variables are shared in threads
g_num = 100
g_num_lst = [100]


# using mutex to execute commands alternately by blocking
mutex = threading.Lock()


def test1(ad_num):
    global g_num
    # strictly guarantee the completeness of the process, less fairly
    # mutex.acquire()  # lock
    for i in range(100000):
        # fairly allocate resources, but the process is not rigorous enough
        mutex.acquire()  # lock
        g_num += ad_num
        mutex.release()  # unlock
    # mutex.release()  # unlock
    print('in test1 g_num=%d' % g_num)


def test2(ad_num):
    global g_num
    for i in range(100000):
        mutex.acquire()  # lock
        g_num += ad_num
        mutex.release()  # unlock
    print('in test2 g_num=%d' % g_num)


def main():
    # target specified the function to be called
    # args(tuple) specified the arguments used in target function
    t1 = threading.Thread(target=test1, args=(1,))
    t2 = threading.Thread(target=test2, args=(1.5,))

    t1.start()
    # time.sleep(0.01)  # main threading sleep 0.5s, sub-threading is running.

    t2.start()
    time.sleep(0.5)

    # while True:
    #     print(threading.enumerate())
    #     if len(threading.enumerate())<=1:
    #         break
    #     time.sleep(1)
    print("in main thread g_num is %d" % g_num)


# inherit Thread class
class MyThread(threading.Thread):
    def task1(self):
        """Any task you want to do within this thread."""
        global g_num
        g_num += 1
        g_num_lst.append(g_num)
        print("in task1 g_num=%d." % g_num)
        print("in task1 g_num_lst is %s." %(str(g_num_lst)))

    def task2(self):
        """Any task you want to do within this thread."""
        print("in task2 g_num=%d." % g_num)
        print("in task2 g_num_lst is %s." %(str(g_num_lst)))


    def run(self):  # Automatically called when the start() is called. Must exist
        # call functions that have been defined within this class
        self.task1()
        self.task2()

        # other things you may want to do


# %%
if __name__ == '__main__':
    main()
    # t = MyThread()
    # t.start()
# %%
