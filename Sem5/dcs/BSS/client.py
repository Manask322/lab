import socket                
import pickle
import sys
from time import sleep
import threading
import select

list_of_ip=None
rank=int(sys.argv[1])
server_port = 8001
buffer=[]
flush=0
inp_flag=0
received_msg=[]
my_clock=None

def get_peers_addr():
    global list_of_ip,rank,server_port
    server = socket.socket()          
    server.connect(('127.0.0.1',server_port))
    list_of_ip=server.recv(1024)
    server.close()
    list_of_ip=pickle.loads(list_of_ip)

def update():
    global my_clock
    for msg in buffer:
        if isvalid(msg):
            print(" recieved after buffer msg: ",msg[1:]," from : ",msg[0],"\n")
            for i in range(len(my_clock)):
                my_clock[i]=max(my_clock[i],msg[1+i])
            buffer.remove(msg)

def listen_thread():
    global my_listen_addr,received_msg,flush,inp_flag
    mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mySock.bind(my_listen_addr)
    while True:
        recv_msg=mySock.recvfrom(1024)
        if isvalid(pickle.loads(recv_msg[0])):     
            received_msg.append(pickle.loads(recv_msg[0]))
            msg=received_msg.pop()
            for i in range(len(my_clock)):
                my_clock[i]=max(my_clock[i],msg[1+i])
            if inp_flag:
                sys.stdout.write('recieving....\n')
            flush=1
            print("recieved msg from : ",msg[0]," msg: ",msg[1:]," myclock ",my_clock,"\n")
            update()
            flush=0
        else:
            buffer.append(pickle.loads(recv_msg[0]))
            if inp_flag:
                sys.stdout.write('recieving.....\n')
            flush=1
            print("Buffered msg : ",buffer[-1][1:]," from process : ",buffer[-1][0]," myclock ",my_clock,"\n")
            flush=0


def isvalid(message):
    global buffer,my_clock
    sr=message[0]
    message=message[1:]
    if(my_clock[sr]!=message[sr]-1):
        return False
    for k in range(len(message)):
        if k!=sr:
            if my_clock[k]>=message[k]:
                pass
            else:
                return False
    return True

def broadcast(msg):
    msg=pickle.dumps(msg)
    process=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(len(list_of_ip)):
        if i!=rank:
            sleep(0.1)
            process.sendto(msg,(list_of_ip[i][0],list_of_ip[i][1]+1))
    process.close()


if __name__ == '__main__':
    get_peers_addr()
    my_clock=[0 for _ in range(len(list_of_ip))]
    my_listen_addr=(list_of_ip[rank][0],list_of_ip[rank][1]+1)
    threading.Thread(target=listen_thread).start()
    print("press whenever you want to broadcast\n")
    while True:
        # if buffer_flag==1:
        #     print("Buffered msg : ",buffer[-1][1:]," from process : ",buffer[-1][0])
        #     buffer_flag=0
        # while(len(received_msg)):
        #     msg=received_msg.pop()
        #     for i in range(len(msg[1:])):
        #         my_clock[i]=max(my_clock[i],msg[i])
        #     print("recieved msg from : ",msg[0]," msg: ",msg[1:])
        inp_flag=1
        inp=input("")
        inp_flag=0
        if inp=='bc':
            my_clock[rank]+=1
            broadcast([rank]+my_clock)
            sleep(0.1)
        elif inp=='bcd':
            my_clock[rank]+=1
            sleep(2)
            broadcast([rank]+my_clock)
            sleep(1)
        else:
            pass