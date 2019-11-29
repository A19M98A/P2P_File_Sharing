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

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Inter host IP : ")
port = input("Inter port : ")
print (host)
print (port)
input()
serversocket.bind((str(host), int(port)))

serversocket.listen(5)
print ('server started and listening')

# (clientsocket, address) = serversocket.accept()
tr = []

while 1:
    (clientsocket, address) = serversocket.accept()
    #print ("connection found!")
    # data = clientsocket.recv(1024).decode()
    processThread = threading.Thread(target = listen, args = (clientsocket,))
    tr.append(processThread)
    processThread.start()
    # print (data)
    # print (clientsocket.type)
    #r='REceieve'
    #clientsocket.send(r.encode())
