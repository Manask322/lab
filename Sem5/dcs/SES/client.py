import socket                
import pickle
import sys
from time import sleep
import threading
import select
import copy

list_of_ip=None
rank=int(sys.argv[1])
server_port = 8001
buffer=[]
flush=0
inp_flag=0
received_msg=[]
my_memory=None
my_clock=None
n=None

def get_peers_addr():
    global list_of_ip,server_port
    server = socket.socket()          
    server.connect(('127.0.0.1',server_port))
    list_of_ip=server.recv(1024)
    server.close()
    list_of_ip=pickle.loads(list_of_ip)

def update():
    global my_clock
    for msg in buffer:
        if isvalid(msg):
            update_clock(msg,msg[0])
            print(" recieved after buffer msg: ",msg[1:]," from : ",msg[0]," myclock ",my_clock,"\n")            
            buffer.remove(msg)


def update_clock(msg,sender):
    global my_memory
    sender_clock=msg[1:n+1]
    for i in range(n):
        my_clock[i]=max(sender_clock[i],my_clock[i])
    recieved_memory=msg[n+1]
    for i in range(n):
        if i!=rank and i!=sender:
            for k in range(len(my_memory[i])):
                my_memory[i][k]=max(my_memory[i][k],recieved_memory[i][k]) 

def listen_thread():
    global my_listen_addr,received_msg,flush,inp_flag,my_clock
    mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mySock.bind(my_listen_addr)
    while True:
        recv_msg=mySock.recvfrom(1024)
        if isvalid(pickle.loads(recv_msg[0])):     
            received_msg.append(pickle.loads(recv_msg[0]))
            msg=received_msg.pop()
            my_clock[rank]+=1
            update_clock(msg,msg[0])
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
    sender_memory_clock=message[n+1][rank]
    for k in range(len(my_clock)):
        if my_clock[k]<sender_memory_clock[k]:
            return False    
    return True

def thread_send(msg,process,p):
    sleep(5)
    process.sendto(msg,(list_of_ip[p][0],list_of_ip[p][1]+1))

def send(msg,delay=False,p=None):
    process=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg=pickle.dumps(msg)
    if delay:
        threading.Thread(target=thread_send,args=(msg,process,p)).start()
    else:
        process.sendto(msg,(list_of_ip[p][0],list_of_ip[p][1]+1))
    my_memory[p]=my_clock[:]


if __name__ == '__main__':
    get_peers_addr()
    n=len(list_of_ip)
    my_clock=[0 for _ in range(n)]
    my_memory=[[0 for _ in range(n)] for _ in range(n)]
    my_listen_addr=(list_of_ip[rank][0],list_of_ip[rank][1]+1)
    t=threading.Thread(target=listen_thread)
    t.start()
    print("enter 'sm:<process_no>' whenever you want to broadcast and 'smd:<process_no>' to make a delay in sm for that process\n")
    try:
        while True:
            inp_flag=1
            inp=input("").split(":")
            inp_flag=0
            if inp[0]=='sm':
                my_clock[rank]+=1
                msg=[rank]+my_clock+[my_memory]
                send(msg,False,int(inp[1]))
            elif inp[0]=='smd':
                my_clock[rank]+=1
                msg=[rank]+my_clock+[my_memory]
                send(msg,True,int(inp[1]))
            else:
                pass
    except KeyboardInterrupt:
        t.join()
        print("Bye!")