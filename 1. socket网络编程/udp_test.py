# -*- coding: utf-8 -*-
"""
@ Author: Brynhildr Wu
@ Email: brynhildrwu@gmail.com

UDP/IP communication test

update: 2022/7/5

"""

# %% load in modules
import socket

# %% udp communication
def send_label(udp):
    dest_ip = input('Please enter ip address:')  # str
    dest_port = int(input('Please enter port:'))  # int
    predict_label = int(input('Please enter predicted label:'))  # int
    udp.sendto(predict_label.encode('gbk'), (dest_ip, dest_port))  # or 'utf-8'


def recv_label(udp):
    predict_label = udp.recvfrom(1024)  # ((ip,port), msg)
    print('%s:%s' % (str(predict_label[1]), str(predict_label[0].decode('gbk'))))


def main():
    # create udp socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # bind address
    local_addr = ('', 8081)
    udp_socket.bind(local_addr)  # only support local address

    # begin communication
    continue_experiment = True
    while continue_experiment:
        send_label(udp_socket)  # sending message
        recv_label(udp_socket)  # receive message

    # close socket
    udp_socket.close()


if __name__ == "__main__":
    main()
