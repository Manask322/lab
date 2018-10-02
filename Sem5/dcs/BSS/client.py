import socket                
import pickle
import sys
from time import sleep
import threading

rank=int(sys.argv[1])
server = socket.socket()          
server_port = 8001
clock=[0,0,0]
list_of_ip=None
server.connect(('127.0.0.1',server_port))

list_of_ip=server.recv(1024)
list_of_ip=pickle.loads(list_of_ip)
msg="hello from "+str(rank)
my_listen_addr=(list_of_ip[rank][0],list_of_ip[rank][1]+1)

def listen_thread():
    global my_listen_addr
    while True:
        mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mySock.bind(my_listen_addr)
        print(mySock.recvfrom(1024))

dummy=1
print("starting thread")
threading.Thread(target=listen_thread).start()
for i in range(len(list_of_ip)):
    if i!=rank:
        process=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # try commenting the below line and check
        sleep(1)
        process.sendto(msg.encode('utf-8'),(list_of_ip[i][0],list_of_ip[i][1]+1))
        process.close()
server.close()
