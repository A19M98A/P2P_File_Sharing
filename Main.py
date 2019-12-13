import socket
import signal
import sys
import threading
import getpass
import os
from os import system, name 

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clients = dict()
tr = []
def listen(clientsocket):
    i = 1
    while True:
        data = clientsocket.recv(1024).decode()
        if data == 'upload':
            print('Donload start')
            f = open("temp.mp4",'wb')
            i += 1
            l = clientsocket.recv(1048576)
            p = 1
            while (str(l[-3:len(l)]) != "b'end'"):
                f.write(l)
                l = clientsocket.recv(1048576)
                p += 1
            f.write(l[0:-4])
            f.close()
            statinfo = os.stat("temp.mp4")
            size = statinfo.st_size
            
            print('Donload finish')

def Conect():
    while 1:
        (clientsocket, address) = serversocket.accept()
        data = clientsocket.recv(1024).decode()
        print (data)
        clients[data.split(' ')[0]] = clientsocket
        processThread = threading.Thread(target = listen, args = (clientsocket,))
        tr.append(processThread)
        processThread.start()

def CList():
    # print(clients)
    for c in clients:
        print(c + ' : ' + str(clients[c].getpeername()) + '\n----------')

def FList():
    pass

def SFile(DClient, file):
    f = open (file, "rb")
    l = f.read(1024)
    while (l):
        s.send(l)
        l = f.read(1024)

print('1> Server')
print('2> Client')

a = input('> ')

if a == '1':
    host = input("Inter host IP : ")
    port = input("Inter port : ") 
    serversocket.bind((str(host), int(port)))
    serversocket.listen(100)
    print ('server started and listening')
    processThread = threading.Thread(target = Conect)
    processThread.start()
    input('continu')
    system('clear')
    while 1:
        system('clear')
        print('1> List of client')
        print('2> List of files\n')
        s = input('> ')

        if s == '1':
            CList()
        elif s == '2':
            FList()
        input('continu')
elif a == '2':
    pass