import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("IP of server : ")
port = input("port of server : ")
name = input("your name : ")

s.connect((str(host),int(port)))
<<<<<<< HEAD
s.send("Ali connected".encode())
#s.close();
messag=""
def ts(str):
   str='Ali > ' + messag
   s.send(str.encode()) 
   data = ''
   #data = s.recv(1024).decode()
while 2:
   messag = input()
   #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   #host ="localhost"
   #port =8000
   #s.connect((host,port))
   ts(s)
   #s.close ()
=======
s.send((name + " connected").encode())

messag=""

def send(st):
    while True:
        messag = input(name + " > ")
        str = name + ' > ' + messag
        st.send(str.encode())

def receive(st):
    while True:
        data = st.recv(1024).dicode()
        print(data)

sendThread = threading.Thread(target = send, args = (s,))
receiveThread = threading.Thread(target = receive, args = (s,))

sendThread.start()
receiveThread.start()

while True:
    pass

>>>>>>> refs/remotes/origin/master
s.close()
