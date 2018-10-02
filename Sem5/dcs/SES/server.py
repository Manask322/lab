import socket
import select
import sys
import pickle
# from thread import *

server_ip=''
server_port=8001
server=socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('',server_port))
server.listen(100)

clients_list=[]
ip_list=[]
while len(ip_list)<3:
    client,addr=server.accept()
    print(addr)
    clients_list.append(client)
    ip_list.append(addr)

data=pickle.dumps(ip_list)
for client in clients_list:
    client.send(data)
    client.close()
server.close()
