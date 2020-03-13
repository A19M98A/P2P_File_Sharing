import socket
import threading
import os
import signal
import sys
import getpass
from os import system, name 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("IP of server : ")
port = input("port of server : ")
name = input("your name : ")

s.connect((str(host),int(port)))
s.send((name + " connected").encode())

messag=""

def send(st):
    while True:
        messag = input('File: ')
        m = 'upload' #name + ' > ' + messag
        st.send(m.encode())
        file = messag
        f = open (file, "rb")
        statinfo = os.stat(file)
        size = statinfo.st_size
        print(size)
        l = f.read(1048576)
        p = 1
        while (l):
            s.send(l)
            l = f.read(1048576)
            p += 1
            # s.send('end'.encode())
        # print(l)
        s.send('end'.encode())

def GetFile(st):
    print('Donload start')
    fname = st.recv(1024).decode()
    f = open(fname + ".mp4",'wb')
    l = st.recv(1048576)
    p = 1
    while (str(l[-3:len(l)]) != "b'end'"):
        f.write(l)
        l = st.recv(1048576)
        p += 1
    # print(l)
    f.write(l[0:-4])
    f.close()
    # SFile(clientsocket)
    print('Donload finish')

def receive(st):
    while True:
        data = st.recv(1024).decode()
        print(data)
        if data == 'file':
            GetFile(st)

sendThread = threading.Thread(target = send, args = (s,))
receiveThread = threading.Thread(target = receive, args = (s,))

sendThread.start()
receiveThread.start()

while True:
    pass

s.close()