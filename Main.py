import socket
import signal
import sys
import threading
import getpass
import os
from os import system, name
import subprocess as sp
import queue

def signal_handler(sig, frame):
    serversocket.close()
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clients = dict()
files = dict()
DC = dict()
tr = []
lfile = list()

def listen(clientsocket):
    i = 1
    while True:
        data = clientsocket.recv(1024).decode()
        if data == 'upload':
            n = len(clients)
            dd = clientsocket.recv(1024)
            print(str(dd)[2:-1])
            sfile = int(str(dd)[2:-1])
            name = str(clientsocket.recv(1024))[2:-1]
            distenation = clientsocket
            qq = queue.Queue()
            temp = [name, sfile, n, qq]
            files[name] = sfile
            lfile.append(temp)
            clientsocket.send('OK'.encode())
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
            # SFile(distenation, "temp.mp4", name)
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
    for f in lfile:
        print(f)
        print('----------')

def SFile(DClient, file, name):
    while True:
        m = 'upload ' + name
        DClient.send(m.encode())
        f = open (file, "rb")
        statinfo = os.stat(file)
        size = statinfo.st_size
        print(size)
        l = f.read(1048576)
        p = 1
        print(DClient.recv(1024).decode())
        while (l):
            DClient.send(l)
            l = f.read(1048576)
            p += 1
            # s.send('end'.encode())
        # print(l)
        DClient.send('end'.encode())

def UploadFile():
    messag = input('File: ')
    m = 'upload' #name + ' > ' + messag
    serversocket.send(m.encode())
    file = messag
    f = open (file, "rb")
    statinfo = os.stat(file)
    size = statinfo.st_size
    print(size)
    serversocket.send(str(size).encode())
    name = input('name: ')
    serversocket.send(name.encode())
    print(serversocket.recv().decode())
    l = f.read(1048576)
    p = 1
    while (l):
        serversocket.send(l)
        l = f.read(1048576)
        p += 1
        # s.send('end'.encode())
    # print(l)
    serversocket.send('end'.encode())

#////////////////////////////////////////////

print('1> Server')
print('2> Client')

a = input('> ')

if a == '1':
    status, result = sp.getstatusoutput('ifconfig | grep "inet " | grep -v 127.0.0.1[2]')
    result = result.split(' ')
    host = result[len(result) - 5]
    inputhost = input('ip address (difalt "' + host + '): ')
    if inputhost != '':
        host = inputhost
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
    host = input("IP of server : ")
    port = input("port of server : ")
    name = input("your name : ")

    serversocket.connect((str(host),int(port)))
    serversocket.send((name + " connected").encode())
    print('connected')
    while 1:
        system('clear')
        print('1> Upload file')
        print('2> Download file\n')
        s = input('> ')

        if s == '1':
            UploadFile()
        elif s == '2':
            pass
        input('continu')