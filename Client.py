import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("IP of server : ")
port = input("port of server : ")
s.connect((str(host),int(port)))
s.send("Amin connected".encode())
#s.close();
messag=""
def ts(str):
   str='amin > ' + messag
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
s.close()
