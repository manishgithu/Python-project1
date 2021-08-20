import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('169.254.213.206',80))
s.listen(5)
socksclients,address=s.accept()
print("Got connection from ",address)

con=True
while(con):
    msg=socksclients.recv(1024) ## message got from client
    msg=msg.decode("utf-8")
    print("\n",msg,"\n")        ## printed msg
    serverMsg=input("Server side >> ")   ## server sending msg to clients
    socksclients.send(serverMsg.encode("utf-8"))
    
     
    
    if(serverMsg=="quit" or serverMsg=="Q" or serverMsg =="q"):
        con=False
        s.close()
