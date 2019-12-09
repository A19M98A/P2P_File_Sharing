import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("IP of server : ")
port = input("port of server : ")
name = input("your name : ")

s.connect((str(host),int(port)))
s.send((name + " connected").encode())

messag=""

def send(st):
    while True:
        messag = input()
        str = name + ' > ' + messag
        st.send(str.encode())

def receive(st):
    while True:
        data = st.recv(1024).decode()
        print(data)

sendThread = threading.Thread(target = send, args = (s,))
receiveThread = threading.Thread(target = receive, args = (s,))

sendThread.start()
receiveThread.start()

while True:
    pass

s.close()
