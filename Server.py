import socket
import signal
import sys
import threading

def signal_handler(sig, frame):
    serversocket.close()
    print('You pressed Ctrl+C!')

    # sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def listen(clientsocket):
    while True:
        data = clientsocket.recv(1024).decode()
        print (data)

def send():
    while True:
        str = input()
        name = str.split('>')[0]
        message = str.split('>')[1]
        clients[name].send(message.encode())

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Inter host IP : ")
port = input("Inter port : ")
serversocket.bind((str(host), int(port)))

serversocket.listen(5)
print ('server started and listening')
print('-------------------')

# (clientsocket, address) = serversocket.accept()
clients = dict()
tr = []

sender = threading.Thread(target = send)
sender.start()

while 1:
    (clientsocket, address) = serversocket.accept()
    data = clientsocket.recv(1024).decode()
    print (data)
    clients[data.split(' ')[0]] = clientsocket
    processThread = threading.Thread(target = listen, args = (clientsocket,))
    tr.append(processThread)
    processThread.start()
    # print (data)
    # print (clientsocket.type)
    #r='REceieve'
    #clientsocket.send(r.encode())
