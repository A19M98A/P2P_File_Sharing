import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Inter host IP : ")
port = input("Inter port : ")
print (host)
print (port)
input()
serversocket.bind((str(host), int(port)))

serversocket.listen(5)
print ('server started and listening')

(clientsocket, address) = serversocket.accept()

while 1:
    (clientsocket, address) = serversocket.accept()
    #print ("connection found!")
    data = clientsocket.recv(1024).decode()
    print (data)
    print (clientsocket.type)
    #r='REceieve'
    #clientsocket.send(r.encode())
