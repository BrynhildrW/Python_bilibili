# -*- coding: utf-8 -*-
"""
@ Author: Brynhildr Wu
@ Email: brynhildrwu@gmail.com

TCP/IP communication test

update: 2022/7/5

"""

# %% load in modules
from http import client
import socket

# %% tcp client
def tcp_client():
    # create tcp socket
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # target address
    server_ip = input('Please enter ip address:')  # str
    server_port = int(input('Please enter port:'))  # int
    server_addr = (server_ip, server_port)

    # connect to server
    tcp_client_socket.connect(server_addr)

    # send data
    send_data = input('Please enter your message:')
    tcp_client_socket.send(send_data.encode('gbk'))

    # close socket
    tcp_client_socket.close()


# %% tcp server
def tcp_server():
    # create tcp socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind local address
    local_addr = ('', 7788)
    tcp_server_socket.bind(local_addr)

    # listen(passive) mode
    tcp_server_socket.listen(128)

    continue_experiment = True
    num = 0
    while continue_experiment:
        # wait for client and create a new socket for it
        client_socket, client_addr = tcp_server_socket.accept()
        print('Welcome new client: ' + str(client_addr))

        while True:
            # receive requirements from client
            recv_data = client_socket.recv(1024)  # already got the target address, only return data
            if not recv_data:  # client is closed | recv_data=None
                print('Thank you! Waiting for next client...')
                break
            else:
                msg = recv_data.decode('gbk')

            # confirm data status
            client_socket.send('Data received!'.encode('gbk'))
            print(msg)
        # finish communication
        client_socket.close()
        num += 1

        # check server status
        if num == 5:
            continue_experiment = False
            print('Up to limit')

    # close server
    tcp_server_socket.close()


# %%
if __name__ == '__main__':
    tcp_server()

