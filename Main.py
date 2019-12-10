import socket
import signal
import sys
import threading
import getpass
from os import system, name 

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clients = dict()
tr = []

def listen(clientsocket):
    while True:
        data = clientsocket.recv(1024).decode()
        print (data)

def Conect():
    # host = input("Inter host IP : ")
    # port = input("Inter port : ") 
    host = '172.20.7.17'
    port = '5006'
    serversocket.bind((str(host), int(port)))
    serversocket.listen(100)
    print ('server started and listening')
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
        print(c + ' : ' + str(clients[c].getpeername()) + '\n----------\n')

def FList():
    pass

print('1> Server')
print('2> Client')

a = input('> ')

if a == '1':
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
else:
    pass