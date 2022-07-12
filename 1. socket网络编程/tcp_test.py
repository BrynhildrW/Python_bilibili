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

# %% functions
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


def downloader():
    # create tcp client socket
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # target address
    server_ip = input('Please enter server IP:')
    server_port = int(input('Please enter server port:'))
    server_addr = (server_ip, server_port)

    # connect to server
    tcp_client_socket.connect(server_addr)

    # send requirements
    file_name = input('Please enter the file name:')
    tcp_client_socket.send(file_name.encode('gbk'))

    # receive & write data into local file
    recv_data = tcp_client_socket.recv(1024*1024)  # 1 MB
    if recv_data:
        with open('[accept]'+file_name, 'wb') as f:
            f.write(recv_data)

    # close client socket
    tcp_client_socket.close()


def send_file_2_client(client_socket, client_addr, recv_data):
    file_name = recv_data.decode('gbk')

    # confirm data status
    confirm_msg = 'Client(%s) want: %s' % (str(client_addr), file_name)
    confirm_msg += '\nPlease wait...'
    print(confirm_msg)

    # open & read target file
    file_content = None
    try:
        f = open(file_name, 'rb')  # open as bytes
        file_content = f.read()
        f.close()
    except Exception as ret:
        print('No relevant data detected(%s)' % file_name)

    # send file to client
    if file_content:
        client_socket.send(file_content)
        print('Data has been sent! Please check.')


def data_server():
    # create tcp socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind local address
    local_addr = ('', 7788)
    tcp_server_socket.bind(local_addr)

    # listen(passive) mode
    tcp_server_socket.listen(128)

    server_on = True
    num = 0
    while server_on:
        # wait for client and create a new tcp socket for it
        client_socket, client_addr = tcp_server_socket.accept()
        num += 1
        print('Welcome new client: ' + str(client_addr))

        client_on = True
        while client_on:
            # receive requirements from client
            recv_data = client_socket.recv(1024)  # already got the target address, only return data

            # check client status
            if not recv_data:  # no more request
                print('Thank you! Waiting for next client...')
                client_on = False
                continue

            # transfer data
            send_file_2_client(client_socket, client_addr, recv_data)
        # finish communication
        client_socket.close()

        # check server status
        if num > 1:
            server_on = False
            print('Up to limit! This server will be closed.')


# %%
if __name__ == '__main__':
    downloader()

