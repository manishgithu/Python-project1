import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('169.254.213.206',80))
##msg="HI this IS MANISH FROM Client side"
##s.send(msg.encode("utf-8"))

con=True

while(con):
    msg=input("Client side >> ")
    s.send(msg.encode("utf-8"))  ## message sent to server first   
    msGot=s.recv(1024)
    msGot=msGot.decode("utf-8")
    print("\n",msGot,"\n")
    if(msg=="quit" or msg=="Q" or msg=="q"):
        con=False
        s.close()
