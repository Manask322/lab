import socket                
import pickle
import sys
import _thread

rank=int(sys.argv[1])
server = socket.socket()          
server_port = 8001
# server=sys.argv[2] 
clock=[0,0,0]
list_of_ip=None
server.connect(('127.0.0.1',server_port))

list_of_ip=server.recv(1024)
list_of_ip=pickle.loads(list_of_ip)
msg="hello from"+str(rank)
my_listen_addr=(list_of_ip[rank][0],list_of_ip[rank][1]+1)

def listen_thread():
    global my_listen_addr
    print(my_listen_addr)
    mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #This is not getting printed
    print("listening...")
    mySock.bind(my_listen_addr)
    print(mySock.recvfrom(1024))

dummy=1
print("starting thread")
_thread.start_new_thread(listen_thread,())
# It is not starting a thread.....
print("sending to p")
for addr in list_of_ip:
    if addr!=list_of_ip[rank]:
        process=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        process.sendto(msg.encode('utf-8'),(addr[0],addr[1]+1))
server.close()