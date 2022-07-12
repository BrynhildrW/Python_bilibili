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
def test1():
    for i in range(5):
        print('---test1---%d' % i)
        time.sleep(1)


def test2():
    for i in range(8):
        print('---test2---%d' % i)
        time.sleep(1)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    # time.sleep(0.05)  # main threading sleep 0.5s, sub-threading is running.
    t2.start()
    
    while True:
        print(threading.enumerate())
        if len(threading.enumerate())<=1:
            break
        time.sleep(1)


# %%
if __name__ == '__main__':
    main()