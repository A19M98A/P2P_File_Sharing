##########################################
#    ______                ______        #
#   /\  _  \  /'\_/`\     /\  _  \       #
#   \ \ \L\ \/\      \    \ \ \L\ \      #
#    \ \  __ \ \ \__\ \    \ \  __ \     #
#     \ \ \/\ \ \ \_/\ \  __\ \ \/\ \    #
#      \ \_\ \_\ \_\\ \_\/\_\\ \_\ \_\   #
#       \/_/\/_/\/_/ \/_/\/_/ \/_/\/_/   #
#                                        #
#    BLOCKCHAIN py python3 (Jan 2020)    #
#                                        #
##########################################


import socket
import signal
import sys
import threading
import getpass
import os
from os import system, name
import subprocess as sp
import queue
import time
import multiprocessing

# contorol for close socket py Ctrl + C key
def signal_handler(sig, frame):
    serversocket.close()
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#defin data structer for save data of client and file
clients = dict()
files = dict()
DC = dict()
tr = []
lfile = list()
uploding = 0

#listen for client data send for upload and download
def listen(clientsocket):
    i = 1
    while True:
        print('lesten for upload')
        data = clientsocket.recv(1024).decode()
        if data == 'upload':
            n = 0
            dd = clientsocket.recv(1024)
            print(str(dd)[2:-1])
            sfile = int(str(dd)[2:-1])
            name = str(clientsocket.recv(1024))[2:-1]
            distenation = clientsocket
            qq = queue.Queue()
            files[name] = sfile
            clientsocket.send('OK'.encode())
            
            print('Donload start')
            l = clientsocket.recv(1048576)
            p = 1
            while (str(l[-3:len(l)]) != "b'end'"):
                #send data to best client
                d = findMin(clientsocket)
                print('part ' + str(p) + ' send to ' + str(d))
                qq.put(d)
                n += 1

                clients[d].send('send'.encode())
                time.sleep(2)
                # print(clients[d].recv(1024).decode())
                clients[d].send((name + "-" + str(p)).encode())
                time.sleep(2)
                # print(clients[d].recv(1024))
                # clients[d].send(l)
                time.sleep(2)
                l = clientsocket.recv(1048576)
                p += 1
                
            temp = [name, sfile, n, qq]
            lfile.append(temp)

            # for in in range(n):
            #     clients[d].send('send'.encode())
            #     print(clients[d].recv(1024))
            #     clients[d].send((name + "-" + str(p)).encode())
            #     print(clients[d].recv(1024))
            #     clients[d].send(l)

            print('Donload finish')

#find minimom client
def findMin(cd):
    min = 10000
    dmin = ''
    for c in DC:
        if cd != clients[c]:
            if DC[c] < min:
                print(dmin)
                dmin = c
                min = DC[c]
    DC[dmin] += 1
    return dmin

#listen to new client and make thread for paraller work
def Conect():
    while 1:
        (clientsocket, address) = serversocket.accept()
        data = clientsocket.recv(1024).decode()
        print (data)
        clients[data.split(' ')[0]] = clientsocket
        DC[data.split(' ')[0]] = 0
        processThread = threading.Thread(target = listen, args = (clientsocket,))
        tr.append(processThread)
        processThread.start()

#print list of clients
def CList():
    # print(clients)
    for c in clients:
        print(c + ' : ' + str(clients[c].getpeername()) + '\n----------')

#print list of file and client that have that file
def FList():
    for f in lfile:
        print(f)
        d = f[3]
        for i in range(d.qsize()):
            dd = d.get()
            d.put(dd)
            print(dd)
        print('----------')

#send part of data to client
def SFile(DClient, data, name):
    pass

#upload File: send file to server client
def UploadFile():
    
    file =  input('File: ')
    m = 'upload' #name + ' > ' + messag
    serversocket.send(m.encode())
    
    f = open (file, "rb")
    statinfo = os.stat(file)
    size = statinfo.st_size
    print(size)
    serversocket.send(str(size).encode())
    name = input('name: ')
    serversocket.send(name.encode())
    # print(serversocket.recv(1024))
    # print(serversocket.recv(1024).decode())
    l = f.read(1048576)
    p = 1
    while (l):
        serversocket.send(l)
        l = f.read(1048576)
        p += 1
        # s.send('end'.encode())
    # print(l)
    serversocket.send('end'.encode())
    uploding = 0

def recivefile():
    print("lesten")
    global uploding
    while 1:
        data = serversocket.recv(1024)
        print(data.decode())
        if data == 'send':
            # serversocket.send('OK'.encode())
            name = serversocket.recv(1024).decode()
            print(name)
        #     serversocket.send('OK'.encode())
            f = open(name + ".block",'wb')
            # l = serversocket.recv(1048576)
            f.write(name)
            f.close()
        # print('<---->')
        # print(data)

#////////////////////////////////////////////
# make a menu for select what is ur rool
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

    processThread = multiprocessing.Process(target = recivefile)
    processThread.start()
    input('OK...')
    while 1:
        system('clear')
        print('1> Upload file')
        print('2> Download file\n')
        s = input('> ')

        if s == '1':
            processThread.terminate()
            UploadFile()
            processThread = multiprocessing.Process(target = recivefile)
            processThread.start()
        elif s == '2':
            pass
        input('continu')